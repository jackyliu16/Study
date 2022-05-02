#include <pthread.h>
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>

#define P sem_wait
#define V sem_post

unsigned long balance = 200;
pthread_mutex_t lock;

void Alipay_withdraw(int amt) {
    pthread_mutex_lock(&lock);
    if (balance >= amt) {
        usleep(1); // unexpected delays
        balance -= amt;
    }
    pthread_mutex_unlock(&lock);
}

void * Talipay() {
    Alipay_withdraw(100);
}

int main() {
    pthread_t p1, p2, p3;
    pthread_mutex_init(&lock, NULL);

    pthread_create(&p1, NULL, Talipay, NULL);
    pthread_create(&p2, NULL, Talipay, NULL);
    pthread_create(&p3, NULL, Talipay, NULL);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);
    printf("balance = %lu\n", balance);
    pthread_mutex_destroy(&lock);
}