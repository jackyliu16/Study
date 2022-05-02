#include <pthread.h>

#define NUMCPUS 1024

/*在多个cpu核需要同时对于一个数据进行操作的时候，为了避免锁对于运行效率的影响，一般采用分层锁的方式，就比如说通过local锁与global锁实现的，逐步更新全局锁的方案，可以有效降低各锁占用率*/

typedef struct counter_t{
    int             global;
    pthread_mutex_t glock;
    int             local[NUMCPUS];
    pthread_mutex_t llock[NUMCPUS];
    int             threshold;       //update frequency
} counter_t;

// init : recode threshold, init locks, init values
//          of all local counts and global count
void init(counter_t *c, int threshold){
    c->threshold = threshold;

    c->global = 0;
    pthread_mutex_init(&c->glock, NULL);

    int i;
    for ( i=0 ; i < NUMCPUS ; i++ ) {
        c->local[i] = 0;
        pthread_mutex_init(&c->llock[i], NULL);
    }
}

// update: usually, just grab local lock and update local amount
//      once local count has risen by 'threshold', grab global
//      lock and transfer local values to it
void update(counter_t *c, int threadID, int amt){
    pthread_mutex_lock(&c->llock[threadID]);
    c->local[threadID] += amt;
    if ( c->local[threadID] >= c->threshold ){
        pthread_mutex_lock(&c->glock);
        c->global += c->local[threadID];
        pthread_mutex_unlock(&c->glock);
        c->local[threadID] = 0;
    }
    pthread_mutex_unlock(&c->llock[threadID]);
}

// get: just return global amount (which may not be perfect)
int get(counter_t *c){
    pthread_mutex_lock(&c->glock);
    int val = c->global;
    pthread_mutex_unlock(&c->glock);
    return val;
}