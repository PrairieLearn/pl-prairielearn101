#pragma once

struct node {
  int value;
  struct node *next;
};

struct list {
  struct node *head;
};

void list_delete_value(struct list *list, int value);
