#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
    int size;
    struct _node *next;
    struct _node *prev;
} Node; 

typedef struct _DoubleLinkedList {
    Node *head;
    Node *tail;
} DLinkedList;

// DoubleLinkedList (non cyclical)
DLinkedList init(){
    DLinkedList list;
    list.head = NULL;
    list.tail = NULL;
    return list;
}

Node* create_item(int number){
    Node *node=(Node *)malloc(sizeof(Node));
    memset(node, 0, sizeof(Node));
    node->next = node->prev = NULL;
    node->size = number;
    return node;
}

// tail interpolation
void *add_item(DLinkedList *pList, Node *item) {
    if ( pList->head == NULL && pList->tail == NULL ) {
        // if empty
        pList->head = item;
        pList->tail = item;
    }
    else if ( pList->head == NULL || pList->tail == NULL ) {
        printf("error 1: head or tail is NULL\n");
    }
    else {
        // wasn't empty
        // item->next = pList->head;
        pList->tail->next = item;
        item->prev = pList->tail;
        pList->tail = item;
    }
}

void delete_value(DLinkedList *pList, int value){
    Node *p, *q;
    for ( q=NULL, p=pList->head; p != NULL ; q=p, p=p->next ) {
        printf("checking %d\n",p->size);

        if ( p->size == value ) {
            printf("finded\n");
            // if find Node
            if ( q == NULL ) {
                // if delete head node
                if ( p->next != NULL ) {
                    pList->head = p->next;
                    pList->head->prev = NULL;
                }
                else {
                    // if LinkedList only have head node, and want to delete
                    pList->head = NULL;
                    pList->tail = NULL;
                }
            }
            else {
                // wasn't delete head node
                if ( p->next != NULL ) { 
                    q->next = p->next;
                    p->next->prev = q;
                }
                else {
                    // delete tail node
                    q->next = NULL;
                    pList->tail = q;
                }
                free(p);
                goto END_OF_Delete;
            }
        }
    }
    printf("haven't find node");
END_OF_Delete:
}

void print_linked_list(const DLinkedList *pList){
    Node *p, *q;
    if ( pList->head == NULL ) {
        printf("empty list\n");
    }
    else {
        for ( p = pList->head; p != NULL; p = p->next ) {
            printf("%d\t", p->size);
        }
    }
    printf("\n");
}

void delete_all(DLinkedList *pList){
    Node *p, *q;
    p = pList->head;
    while ( p != NULL ) {
        q = p->next;
        free(p);
        p = q;
    }
    pList->head = NULL;
    pList->tail = NULL;
    printf("completed delete\n");
}

int main(void) {
    DLinkedList list = init();
    int number;
    Node *tmp;
    scanf("%d", &number);
    do {
        if ( number != -1 ) {
            tmp = create_item(number);
            add_item(&list, tmp);
            scanf("%d", &number);
        }
    } while ( number != -1 );

    print_linked_list(&list);
    delete_all(&list);
    print_linked_list(&list);


}
