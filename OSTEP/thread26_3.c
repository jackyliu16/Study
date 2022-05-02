#include <stdio.h>
#include <pthread.h>

static volatile int counter = 0;

void *mythread2(void *arg){
    printf("%s:begin\n", (char *) arg);
    int i;
    for ( i = 0 ; i < 1e7 ; i++ ) {
        counter += 1;
    }
    printf("%s:done\n", (char *)arg);
    return NULL;
}

int main(){
    pthread_t p1, p2;
    printf("main: begin(counter = %d)\n", counter);
    pthread_create(&p1, NULL, mythread2, "A");
    pthread_create(&p2, NULL, mythread2, "B");

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    printf("main: done with both (counter = %d)\n", counter);
    return 0;
}