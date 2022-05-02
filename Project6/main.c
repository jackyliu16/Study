#include <stdio.h>
#include <stdbool.h>



#define SIZE 1024;

typedef struct {
    int size;
    void *data;
} memory_block;

typedef struct node{
    struct node *prior;
    bool hasBeenUsed;
    memory_block *data;
    struct node *next;
} LinkedList;


void init(){
    LinkedList *head, *node;
    head = (LinkedList *)malloc(sizeof(LinkedList));
    
    node = (LinkedList *)malloc(sizeof(LinkedList));
    node->prior = head;
    node->hasBeenUsed=false;
    node->data = (memory_block *)malloc(sizeof(memory_block));
        node->data->size = 1024;
    node->next = NULL;

    head->next = node;
}




int main(int argc, char const *argv[])
{
    init();


    
    


    return 0;
}
