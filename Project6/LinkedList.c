#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct  _Node {
	int data ; 
	struct _Node *next ;
} Node ;
 
// 单向带头结点的链表
typedef struct _LinkedList{
    Node *head ;
    Node *end ;
} LinkedList; 	

// memset(new_list,0,sizeof(LinkedList));          // malloc 后所得到的空间是脏的

void print_linked_list(LinkedList *list){
    Node *p;
    for ( p = list->head->next; p != NULL; p = p->next ){
        printf("%d\t", p->data);
    }
}

void add_Node(LinkedList * list, const int num){
    Node *new_Node = (Node *)malloc(sizeof(Node));
    new_Node->data = num;
    new_Node->next = NULL;

    list->end->next = new_Node;
    list->end = new_Node;
}



int main(void)
{
    LinkedList list;
    Node *node = (Node *)malloc(sizeof(Node));
    list.head = list.end = node;

    add_Node(&list, 10);
    add_Node(&list, 20);
    print_linked_list(&list);



    return 0;
}