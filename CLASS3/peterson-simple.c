/*
设计原理：
    想进入临界区之前，A/B都要举起自己的旗子
        A举好旗子之后，往门上贴B正在使用的标签
        B                   A
    然后，如果对方的旗子举起来之后，并且门上的名字不是自己，
        等待
    否则
        可以进入临界区
    出包厢后，放下自己的旗子
*/

#include "thread.h"

#define A 1
#define B 2

atomic_int nested;
atomic_long count;

void critical_section() {
  long cnt = atomic_fetch_add(&count, 1);     // 原子的对于一个计数器++
  assert(atomic_fetch_add(&nested, 1) == 0);  // 如果计数器为2->两个进程同时进入临界区
  atomic_fetch_add(&nested, -1);
}

int volatile x = 0, y = 0, turn = A;

void TA() {
    while (1) {
/* PC=1 */  x = 1;
/* PC=2 */  turn = B;
/* PC=3 */  while (y && turn == B) ;
            critical_section();
/* PC=4 */  x = 0;
    }
}

void TB() {
  while (1) {
/* PC=1 */  y = 1;
/* PC=2 */  turn = A;
/* PC=3 */  while (x && turn == A) ;
            critical_section();
/* PC=4 */  y = 0;
  }
}

int main() {
  create(TA);
  create(TB);
}
