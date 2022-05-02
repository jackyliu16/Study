#include"thread.h"
#include<stdio.h>

int sum = 0;
int N = 20000;

void Tsum(){
    for ( int i = 0 ; i < N ; i++ ) {
        sum++;      // SUM++是由四条指令实现的
        // 如果想要实现转换成为一条汇编代码:asm volatile("add $1, %0":"+m"(sum)); 更进一步可以在add前加lock
    }
}

int main(){
    create(Tsum);
    create(Tsum);

    join();
    printf("%d", sum);
}