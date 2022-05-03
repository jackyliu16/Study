#include "thread.h"
#include "thread-sync.h"

#define N 3
sem_t locks[N];

// BUG_REPORT: 这个地方会出现死锁的原因是如果无法进入下一步不会先返回信号量
void Tphilosopher(int id) {
  int lhs = (N + id - 1) % N;
  int rhs = id % N;
  while (1) {
    P(&locks[lhs]);
    printf("T%d Got %d\n", id, lhs + 1);  
    P(&locks[rhs]);
    printf("T%d Got %d\n", id, rhs + 1);
    V(&locks[lhs]);
    V(&locks[rhs]);
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
