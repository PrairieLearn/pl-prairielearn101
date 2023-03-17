#include <stdlib.h>
#include "list.h"

void list_delete_value(struct list *list, int value) {

    struct node *prev = NULL;
    struct node *cur = list->head;

    while (cur) {
        if (cur->value == value) {
           if (prev)
                prev->next = cur->next;
           else
               list->head = cur->next;
           free(cur);
        } else {
            prev = cur;
        }
        cur = cur->next;
    }
}
