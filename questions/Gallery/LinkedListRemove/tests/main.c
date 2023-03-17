#include <stdlib.h>
#include <check.h>
#include <time.h>
#include <stdarg.h>
#include <sanitizer/asan_interface.h>

#include "list.h"

static void asan_abort_hook(const char *msg) {
  ck_abort_msg("Detected an error in the use of pointers and dynamic allocation. This is \n"
               "typically related to the use of values in the heap (malloc and friends) \n"
               "after free or beyond their allocated area, or freeing a value not in the heap.\n"
               "Details:\n\n%s", msg);
}

struct node *original_pointers[1024];
int original_values[1024];

void generic_test(int search_value, ...) {

  struct list *l = malloc(sizeof(struct list));
  l->head = NULL;
  struct node **tail = &l->head;

  va_list elements;
  va_start(elements, search_value);
  int value_add;
  int pos = 0;
  while ((value_add = va_arg(elements, int)) != -1) {
    struct node *n = malloc(sizeof(struct node));
    n->value = value_add;
    n->next = NULL;
    *tail = n;
    tail = &n->next;
    original_pointers[pos] = n;
    original_values[pos] = value_add;
    pos++;
  }
  original_pointers[pos] = NULL;
  original_values[pos] = search_value + 1;

  list_delete_value(l, search_value);

  struct node *prev = l->head;
  for (int i = 0; i < pos; i++) {
    if (original_values[i] == search_value) {
      ck_assert_msg(prev != original_pointers[i],
                    "Next pointer of previous node was not updated, "
                    "node that was to be deleted is still in the list.");
      ck_assert_msg(__asan_address_is_poisoned(original_pointers[i]),
                    "Deleted node was not ");
    } else {
      ck_assert_msg(prev == original_pointers[i],
                    "Original node with a value that does not match "
                    "the search value is no longer in the list.");
      ck_assert_msg(original_values[i] == original_pointers[i]->value,
                    "Value of original node was modified.");
      struct node *next = prev->next;
      free(prev);
      prev = next;
    }
  }
  ck_assert_msg(prev == NULL, "Next pointer of last element is not NULL.");
  free(l);
}

START_TEST(test_no_deletes) {

  generic_test(5, -1);
  generic_test(12, 5, 3, 10, 11, 13, 5, 10, 90, -1);
}
END_TEST

START_TEST(test_delete_one) {

  generic_test(5, 5, -1);
  generic_test(12, 12, 5, 3, 10, 11, 13, 5, 10, 90, -1);
  generic_test(90, 12, 5, 3, 10, 11, 13, 5, 10, 90, -1);
  generic_test(11, 12, 5, 3, 10, 11, 13, 5, 10, 90, -1);
}
END_TEST

START_TEST(test_delete_multiple) {

  generic_test(12, 12, 5, 3, 10, 12, 13, 5, 10, 90, -1);
  generic_test(90, 12, 5, 90, 10, 11, 13, 5, 10, 90, -1);
  generic_test(11, 11, 5, 3, 10, 11, 13, 5, 10, 11, -1);
}
END_TEST

START_TEST(test_delete_consecutive) {

  generic_test(5, 5, 5, 5, -1);
  generic_test(12, 12, 12, 12, 10, 15, 13, 5, 10, 90, -1);
  generic_test(90, 12, 5, 90, 10, 11, 13, 90, 90, 90, -1);
  generic_test(11, 11, 5, 3, 11, 11, 11, 5, 10, 11, -1);
}
END_TEST

int main(int argc, char *argv[]) {

  __asan_set_error_report_callback(asan_abort_hook);

  Suite *s = suite_create("Linked list");

  TCase *tc = tcase_create("Lists that don't contain the value");
  tcase_add_test(tc, test_no_deletes);
  suite_add_tcase(s, tc);

  tc = tcase_create("Lists that contain the value once");
  tcase_add_test(tc, test_delete_one);
  suite_add_tcase(s, tc);
  
  tc = tcase_create("Lists that contain the value multiple times");
  tcase_add_test(tc, test_delete_multiple);
  suite_add_tcase(s, tc);
  
  tc = tcase_create("Lists that contain the value in consecutive positions");
  tcase_add_test(tc, test_delete_consecutive);
  suite_add_tcase(s, tc);
  
  SRunner *sr = srunner_create(s);
  
  srunner_run_all(sr, CK_NORMAL);
  srunner_free(sr);
  return 0;
}
