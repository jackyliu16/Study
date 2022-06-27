#include "pthread.h"
#include "thread-sync.h"
#include "thread.h"
#include <semaphore.h>
#include <stdio.h>

#define N 12
sem_t locks[N];
mutex_t lock;

void Philosopher(int i) {
  int lhs = (N + i - 1) % N;
  int rhs = i % N;

  if (i == 1) {
    mutex_lock(&lock);
    P(&locks[lhs]);
    P(&locks[rhs]);
    mutex_unlock(&lock);

    printf("%d\n", i);

    mutex_lock(&lock);
    P(&locks[lhs]);
    V(&locks[rhs]);
    mutex_unlock(&lock);
  } else {
    mutex_lock(&lock);
    P(&locks[rhs]);
    P(&locks[lhs]);
    mutex_unlock(&lock);

    printf("%d\n", i);

    mutex_lock(&lock);
    P(&locks[lhs]);
    V(&locks[rhs]);
    mutex_unlock(&lock);
  }
}

int main() {
  for (int i = 0; i < N; i++) {
    SEM_INIT(&locks[i], 0);
  }
  for (int i = 0; i < N; i++) {
    create(Philosopher);
  }
}
