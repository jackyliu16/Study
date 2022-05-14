#include "thread.h"
#include "thread-sync.h"

#define N 3
sem_t locks[N];
mutex_t mutex;

// BUG_REPORT: 这个地方会出现死锁的原因是如果无法进入下一步不会先返回信号量[C语言不提供对应的机制]
void Tphilosopher(int id) {
    int lhs = (N + id - 1) % N;
    int rhs = id % N;
    int time = 10;
    while ( time-- > 0 ) {

        mutex_lock(&mutex);
        printf("a %d\n", id);
        P(&locks[lhs]);
        P(&locks[rhs]);
        mutex_unlock(&mutex);
        
        printf("id %d eating\n", id);

        mutex_lock(&mutex);
        printf("b %d\n", id);
        V(&locks[rhs]);
        V(&locks[lhs]);
        mutex_unlock(&mutex);
        
        printf("id %d thinking\n", id);
    }


}

int main(int argc, char *argv[]) {
    for (int i = 0; i < N; i++) {
        SEM_INIT(&locks[i], 1);
    }
    for (int i = 0; i < N; i++) {
        create(Tphilosopher);
    }
}