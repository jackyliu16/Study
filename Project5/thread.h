#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdatomic.h>
#include <assert.h>
#include <unistd.h>
#include <pthread.h>

#define NTHREAD 64
enum { T_FREE = 0, T_LIVE, T_DEAD, };
struct thread {
  int id, status;
  pthread_t thread;
  void (*entry)(int);
};

struct thread tpool[NTHREAD], *tptr = tpool;

void *wrapper(void *arg) {
  struct thread *thread = (struct thread *)arg;
  thread->entry(thread->id);
  return NULL;
}

/*
 * 创建了一个入口函数为fn的线程，并且立即开始执行
 * 	void fn(int tid){...}
 * 	tid start with 1
 * 语义：在状态中新增stack frame列表并且初始化为fn(tid)
 * */
void create(void *fn) {
  assert(tptr - tpool < NTHREAD);
  *tptr = (struct thread) {
    .id = tptr - tpool + 1,
    .status = T_LIVE,
    .entry = fn,
  };
  pthread_create(&(tptr->thread), NULL, wrapper, tptr);
  ++tptr;
}

/*
 * 等待所有正在运行的进程的fn返回
 * 在main返回的时候会自动等待所有线程结束
 * 语义： 在其他线程还没有执行完时死循环，不会进入下一个状态
 * 		执行完成后返回
 * 注意：编译的时候需要添加 -lphread [调用了posthreads的线程库]
 * */
void join() {
  for (int i = 0; i < NTHREAD; i++) {
    struct thread *t = &tpool[i];
    if (t->status == T_LIVE) {
      pthread_join(t->thread, NULL);
      t->status = T_DEAD;
    }
  }
}

__attribute__((destructor)) void cleanup() {
  join();
}
