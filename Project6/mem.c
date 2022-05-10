#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define KB 1024 

typedef struct _node {
    int size ;
    bool hasBeenUsed;
    struct _node *next ;
    struct _node *prev ;
} Node;

typedef struct _memory_block {
    Node *head;
    Node *tail;
} MemoryBlock;

MemoryBlock* init(){
    MemoryBlock *block = malloc(sizeof(MemoryBlock));
    // memset(&block, 0, sizeof(MemoryBlock));

    Node *node = (Node *)malloc(sizeof(Node));
    node->size = 64;
    node->next = node->prev = NULL;

    block->head = node;
    block->tail = node;
    return block;
}

// split a node into two pieces
void split_node(MemoryBlock *pList, Node *split_node, int want_value, Node *result_fragment){
    result_fragment = (Node *)malloc(sizeof(Node));
    result_fragment->hasBeenUsed  = false;
 
    // memset(&result_fragment, 0, sizeof(Node));
   
    if ( split_node-> size < want_value ) {
        printf("haven't enough space for fragment");
        return;
    }

    result_fragment->size = split_node->size - want_value;
    split_node->size = want_value;

    // if it is the only item in linked list

    // if have next
    if ( split_node->next != NULL ) {
        split_node->next->prev = result_fragment;
        result_fragment->next = split_node->next;
        split_node->next = result_fragment;
        result_fragment->prev = split_node;    
    }
    else if ( pList->tail == split_node ) {
        split_node->next = result_fragment;
        result_fragment->prev = split_node;
        pList->tail = result_fragment;
    }
    // // if have prev
    // if ( split_node->prev != NULL ) {
        
    // }
    printf("end");
}

void print_memory_allocation( MemoryBlock *pBlock) {
    printf("\nOUTPUT:\n");
    Node *p, *q;
    for ( p = pBlock->head; p != NULL; p =p->next ) {
        printf("%d\t", p->size);
    }
    printf("\n");
    for ( p = pBlock->head; p != NULL; p =p->next ) {
        printf("%d\t", p->hasBeenUsed);
    }
    printf("\n");

}

void ask_for_memory(MemoryBlock *block, int value) {
    // from head to tail find a space which contails areas >= need and hasn't been used yet
    Node *p = block->head, *q;
    // delete the node and try to split it into two parts
    // one parts is matching the need, and others parts are (total - value)
    while ( p != NULL ) {
        if ( p->size >= value ) {
            split_node(block, p, value, q);
            p->hasBeenUsed = true;
            break;
        }
        p=p->next;
    }
}

void release_memory(MemoryBlock *block, Node *release ) {
    release->hasBeenUsed = false;

    Node *p, *q, *s;
    // if prev is unused
    if ( release->next && ! release->next->hasBeenUsed ) {
        release->size += release->next->size;
        if ( release->next->next ) {
            release->next = release->next->next;
            release->next->prev = release;
        }
        else {
            release->next = NULL;
            block->tail = release;
        }
        free(release->next);
    }

    // if next is unused
    if ( release->prev && !release->prev->hasBeenUsed ) {
        release->size += release->next->size;

        if ( release->prev->prev ) {
            release->prev = release->prev->prev;
            release->prev->next = release;
        }
        else {
            release->prev = NULL;
            block->head = release;
        }
    }
}

int main(){
    MemoryBlock *block = init();
    ask_for_memory(block, 20);
    ask_for_memory(block, 5);
    ask_for_memory(block, 30);
    release_memory(block, block->head);
    
    print_memory_allocation(block);
}