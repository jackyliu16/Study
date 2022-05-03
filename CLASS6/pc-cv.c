#include "thread.h"
#include "thread-sync.h"

int n, count = 0;
mutex_t lk = MUTEX_INIT();              // mutex_lock
cond_t pro = COND_INIT(), con = COND_INIT();

/* Algroithm: 提供的算法[此处有点类似于记录型信号量的保存方式]
需要等待条件满足时:
        mutex_lock(&mutex);
        while (!cond) {
          wait(&cv, &mutex);
        }
        assert(cond);
        // ...
        // 互斥锁保证了在此期间条件 cond 总是成立
        // ...
        mutex_unlock(&mutex);
其他线程条件可能被满足时
        broadcast(&cv);
*/

void Tproduce() {
  while (1) {
    mutex_lock(&lk);      // lock to makesure everythings doing alone
    while (!(count != n)) {
      cond_wait(&pro, &lk);
      // if lk is lock than sleep until someone wake you up(signaled or broadcast) and has a &cv
                          // Wait for condition variable COND to be signaled or broadcast. MUTEX is assumed to be locked before.
    }
    assert(count != n);
    printf("("); count++;
    // cond_signal(&con);
    cond_broadcast(&con);
    mutex_unlock(&lk);
  }
}

void Tconsume() {
  while (1) {
    mutex_lock(&lk);
    while (!(count != 0)) {
      cond_wait(&con, &lk); // 
    }
    assert(count != 0);             // check if bug is not empty
    printf(")"); count--;
    cond_broadcast(&pro);
    mutex_unlock(&lk);
  }
}

int main(int argc, char *argv[]) {
  assert(argc == 2);
  n = atoi(argv[1]);
  setbuf(stdout, NULL);
  for (int i = 0; i < 8; i++) {
    create(Tproduce);
    create(Tconsume);
  }
}


/* error: Tconsume could wake up Tproduce
void Tproduce() {
  while (1) {
    mutex_lock(&lk);      // lock to makesure everythings doing alone
    if (count == n) {
      cond_wait(&cv, &lk);
      // if lk is lock than sleep until someone wake you up(signaled or broadcast) and has a &cv
                          // Wait for condition variable COND to be signaled or broadcast. MUTEX is assumed to be locked before.
    }
    assert(count != n);
    printf("("); count++;
    cond_signal(&cv);
    mutex_unlock(&lk);
  }
}

void Tconsume() {
  while (1) {
    mutex_lock(&lk);
    if (count == 0) {
      pthread_cond_wait(&cv, &lk);
    }
    printf(")"); count--;
    cond_signal(&cv);
    mutex_unlock(&lk);
  }
}
*/