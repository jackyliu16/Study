#include <stdio.h>
#include <stdlib.h>
#include "thread.h"

#define YES 1
#define NO  0

// int table = YES;

int xchg(volatile int *addr, int newval){
    int result;
    asm volatile ("lock xchg %0, %1":"+m"(*addr), "=a"(result) :"l"(newval));
    return result;
}

int locked = 0;
void lock() { while (xchg(&locked, 1)) ; }
void unlock() { xchg(&locked, 0) ; }

// void lock() {
// int got;
// retry:
//   got = xchg(&table, NO);
//   if (got == NO)
//     goto retry;
//   assert(got == YES);
// }

// void unlock() {
//   xchg(&table, YES);
// }



int bank_account = 100;

void Alipay_withdraw(int amt) {
    lock();
    if (bank_account >= amt) {
        usleep(1); // unexpected delays
        bank_account -= amt;
    }
    unlock();
}

void Talipay(int id) {
  Alipay_withdraw(100);
}

int main() {
  create(Talipay);
  create(Talipay);
  join();
  printf("balance = %d\n", bank_account);
}