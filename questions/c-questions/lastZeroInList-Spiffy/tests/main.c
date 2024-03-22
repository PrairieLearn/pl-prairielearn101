#include <check.h>

extern int foo(int x[], int len);

START_TEST(test_one)
{
    int values[] = {0};
    ck_assert_int_eq(foo(values, 1), 0);
}
END_TEST

START_TEST(test_two)
{
    int values[] = {0, 0, 0, 0};
    ck_assert_int_eq(foo(values, 4), 3);
}
END_TEST

START_TEST(test_three)
{
    int values[] = {0, 1, 2, 3, 0, 4};
    ck_assert_int_eq(foo(values, 6), 4);
}
END_TEST

START_TEST(test_four)
{
    int values[] = {0, 1, 2, 3, 4, 5};
    ck_assert_int_eq(foo(values, 6), 0);
}
END_TEST

int main(int argc, char *argv[])
{

    Suite *s = suite_create("Foo");

    TCase *tc_one = tcase_create("Testing foo(values, 1) where values = {0}");
    tcase_add_test(tc_one, test_one);
    suite_add_tcase(s, tc_one);

    TCase *tc_two = tcase_create("Testing foo(values, 4) where values = {0, 0, 0, 0}");
    tcase_add_test(tc_two, test_two);
    suite_add_tcase(s, tc_two);

    TCase *tc_three = tcase_create("Testing foo(values, 6) where values = {0, 1, 2, 3, 0, 4}");
    tcase_add_test(tc_three, test_three);
    suite_add_tcase(s, tc_three);

    TCase *tc_four = tcase_create("Testing foo(values, 6) where values = {0, 1, 2, 3, 4, 5}");
    tcase_add_test(tc_four, test_four);
    suite_add_tcase(s, tc_four);

    SRunner *sr = srunner_create(s);
    srunner_run_all(sr, CK_NORMAL);
    srunner_free(sr);
    return 0;
}
