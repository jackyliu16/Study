#include <stdio.h>
#include "thread-sync.h"
#include "thread.h"
#include <time.h>
#include <stdbool.h>

#define N 5

mutex_t locked = MUTEX_INIT();
bool avail[N];
cond_t cond;


void eating(int pid){
    int lch = (pid-1-1+N)%N;
	int rch = pid-1;

    // get the chopsticks
    mutex_lock(&locked);
    // if not match then sleep until condition is met
    while (!avail[lch] || !avail[rch]) {
        wait(&cond, &locked);
    }
    avail[lch] = avail[lch] = false;
    printf("people %d using ch %d and %d to eat\n", pid-1, lch, rch);
    sleep(1);
    mutex_unlock(&locked);

    // return chopsticks
    mutex_lock(&locked);
    avail[lch] = avail[rch] = true;
    cond_broadcast(&cond);
    mutex_unlock(&locked);
}


void init(){
    for ( int i =0 ; i < N ; i++ ) {
        // SEM_INIT(&chopsticks[i], 1);
		avail[i] = true;
    }
}

int main(){
    init();
    for (int i = 0; i < N; i++) {
        // usleep(rand()*10);
        printf("create %d\n", i);
        create(eating);
    } 
}
