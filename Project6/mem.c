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
    Node *node = (Node *)malloc(sizeof(Node));
    if ( block == NULL ) {
        printf("error[3]: Failed to allocate memory");
        return NULL;
    }
    if ( node == NULL ) {
        printf("error[3]: Failed to allocate memory");
        return NULL;
    }
    // memset(&block, 0, sizeof(MemoryBlock));

    node->size = 64*KB;
    node->next = node->prev = NULL;

    block->head = node;
    block->tail = node;
    return block;
}

// split a node size into two nodes and the size of want_value is the node split_node's value
void split_node(MemoryBlock *pList, Node *split_node, int want_value, Node *result_fragment);
//[FF] from head sequential search to find the size which could matching the need
void ask_for_memory(MemoryBlock *block, int value);
// print out the allocated memory
void print_memory_allocation(const MemoryBlock *pBlock);
// release memory from designated location
void release_memory(MemoryBlock *block, Node *release );
// asking for release memory from specified index
void ask_for_release(MemoryBlock *block, int pid);
// get the index of MemoryBlock
int length_account(MemoryBlock *block);

int main(int *argc, char **argv){
    MemoryBlock *block = init();
    ask_for_memory(block, 20*KB);
    ask_for_memory(block, 10*KB);
    ask_for_memory(block, 15*KB);
    // ask_for_memory(block, 20*KB);
    ask_for_memory(block, 10*KB);
    print_memory_allocation(block);
    ask_for_release(block, 1);
    print_memory_allocation(block);
    ask_for_release(block, 2);
    print_memory_allocation(block);
    ask_for_release(block, 1);
    print_memory_allocation(block);
}

void ask_for_release(MemoryBlock *block, int pid){
    int length = length_account(block);
    if ( pid >= length ) {
        printf("pid not existed");
        return;
    }
    int account = 0;
    Node *p = block->head;
    while ( p != NULL && account == pid-1 ){
        account ++;
        p=p->next;
    }
    if ( !p->hasBeenUsed ) {
        printf("this memory peace hasn't been used yet\n");
        return ;
    }
    release_memory(block, p);
}

void release_memory(MemoryBlock *block, Node *release ) {
    release->hasBeenUsed = false;

    Node *p;
    // if prev is unused
    if ( release->next && ! release->next->hasBeenUsed ) {
        p = release->next;
        release->size += release->next->size;
        if ( release->next->next ) {
            release->next = release->next->next;
            release->next->prev = release;
        }
        else {
            release->next = NULL;
            block->tail = release;
        }
        free(p);
    }

    // if next is unused
    if ( release->prev && !release->prev->hasBeenUsed ) {
        release->size += release->next->size;
        p = release->prev;
        if ( release->prev->prev ) {
            release->prev = release->prev->prev;
            release->prev->next = release;
        }
        else {
            release->prev = NULL;
            block->head = release;
        }
        free(p);
    }
}

int length_account(MemoryBlock *block) {
    int account = 0;
    Node *p = block->head;
    while( p != NULL ) {
        account ++;
        p = p->next;
    }
    return account;
}

void print_memory_allocation(const MemoryBlock *pBlock) {
    int account = 0 ;
    printf("\nOUTPUT:\nsize:\t");
    Node *p, *q;
    for ( p = pBlock->head; p != NULL; p =p->next ) {
        printf("%d\t", p->size);
        account ++;
    }
    printf("\nused:\t");
    for ( p = pBlock->head; p != NULL; p =p->next ) {
        printf("%d\t", p->hasBeenUsed);
    }
    printf("\npid:\t");
    for ( int i = 0 ; i < account ; i++ ) {
        printf("%d\t", i);
    }
    printf("\n");
}

void ask_for_memory(MemoryBlock *block, int value) {
    // from head to tail find a space which contails areas >= need and hasn't been used yet
    Node *p = block->head, *q;
    // delete the node and try to split it into two parts
    // one parts is matching the need, and others parts are (total - value)
    while ( p != NULL ) {
        if ( !p->hasBeenUsed && p->size >= value ) {
            split_node(block, p, value, q);
            p->hasBeenUsed = true;
            return ;
        }
        p=p->next;
    }
    printf("error[4]: haven't enought space for allocate {memory:%d}\n", value);
}

// split a node into two pieces
void split_node(MemoryBlock *pList, Node *split_node, int want_value, Node *result_fragment) {
    result_fragment = (Node *)malloc(sizeof(Node));
    if ( result_fragment == NULL ) {
        printf("error[3]: Failed to allocate memory for result_fragment\n");
    }
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
}