#include <stdio.h>



typedef struct student{
    int score;
    struct student *next;
} LinkedList;

LinkedList *create(int n){
    LinkedList *head, *node, *end;
    head = (LinkedList *)malloc(sizeof(LinkedList));
    end = head;
    for ( int i = 0 ; i < n ; i++ ) {
        node = (LinkedList *)malloc(sizeof(LinkedList));
        scanf("%d", &node->score);
        end->next = node;
        end = node;
    }
    end->next = NULL;
    return head;
}