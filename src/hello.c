#include <stdio.h>

int main(){
    printf("hello, world!");
    int count = 0;
    for ( int i = 0 ; i < 10 ; i++ ) {
        count++;
    }
    printf("%d", count);
    return 0;
}