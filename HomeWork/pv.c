#include "thread.h"
#include "thread-sync.h"

#define N 3
sem_t locks[N];
mutex_t mutex;

void Tphilosopher(int id) {
    int lhs = (N + id - 1) % N;
    int rhs = id % N;
    int time = 10;
    int count_of_complete = 0;
    while ( time-- > 0 ) {
        // 通过破坏循环等待的方式实现消除死锁
        if ( id == 1 ) {
            P(&locks[lhs]);
            P(&locks[rhs]);
            printf("%d eatting\n", id);
            sleep(1);
            V(&locks[rhs]);
            V(&locks[lhs]);
        }
        else {
            P(&locks[rhs]);
            P(&locks[lhs]);
            printf("%d eatting\n", id);
            V(&locks[lhs]);    
            V(&locks[rhs]);
        }
        printf("id %d thinking\n", id);
        count_of_complete++;
        sleep(2);
    }
    printf("==========%d==========\n", count_of_complete);

}

int main(int argc, char *argv[]) {
    for (int i = 0; i < N; i++) {
        SEM_INIT(&locks[i], 1);
    }
    for (int i = 0; i < N; i++) {
        create(Tphilosopher);
    }
}