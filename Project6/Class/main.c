#include "node.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void add(List *pList, int number);
void print_linked_list(List *pList);
bool find_in_linked_list(List *pList, int number);

int main(int argc, char *argv[]){
    List list;
    int number;
    list.head = NULL;
    do {
        scanf("%d", &number);
        if ( number != -1 ) {
            add(&list, number);
        }
    } while ( number != -1) ;
    
    print_linked_list(&list);
    
    

    return 0;

}

void drop_linked_list(List *list) {
    Node *p, *q;
    for ( p = list ; p ; p = q ) {
        q = p->next;
        free(p);
    }
}

void delete_item(List *pList, int number) {
    Node *q, *p;
    for ( q=NULL, p= pList->head; p ; q=p, p=p->next ) {
        if ( p->value == number ) {
            if ( q ) {
                q->next = p->next;
            }
            else {
                pList->head = p->next;
            }
            free(p);
            break;
        }
    }
}

void print_linked_list(List *pList) {
    Node *p;
    for ( p=pList->head ; p ; p = p->next ) {
        printf("%d\t", p->value);
    }
}

void add(List *pList, int number){
    // add to linked-list
    Node *p = (Node *)malloc(sizeof(Node));
    p->value = number;
    p->next = NULL;
    // find last node in linked
    Node *last = pList->head;
    if ( last != NULL ) {
        while ( last->next != NULL ) {
            last = last->next;
        }
        // attach node to last node
        last->next = p;
    }
    else {
        pList->head = p;
    }
}

bool find_in_linked_list(List *pList, int number){
    Node *p;
    int isFound = 0;
    for ( p=pList->head; p ; p=p->next ) {
        if ( p->value == number ) {
            printf("get");
            isFound = 1;
            break;
        }
    }
    if ( !isFound ) {
        printf("no found");
    }
    return isFound;
}



