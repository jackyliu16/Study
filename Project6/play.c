#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MB 1024*1024

typedef struct _memory_block {
    int size;
    char *data;
} memory_block;

typedef struct _node {
    struct _node *prior;
    bool hasBeenUsed;
    memory_block *data;
    struct _node *next;
} Node;

int main(){
    // memory_block test;
    // char data[MB*1] = {0};
    // test.data = *data;
    // 想法是通过使用一个链表来实现内存的分配功能
    

}
