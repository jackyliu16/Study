#include "thread-sync.h"
#include "thread.h"
#include <pthread.h>
#include <stdio.h>

mutex_t write_reader, mutex;
int reader_number;
sem_t reader;

void reader(int id) {
  mutex_lock(&mutex);
  if (reader_number > 0) {
    mutex_lock(&write_reader);
    reader_number++;
  }
  mutex_unlock(&mutex);

  // reading
  printf("reading with %d guys ", reader_number);

  mutex_lock(&mutex);
  if (reader_number == 1) {
    mutex_unlock(&write_reader);
    reader_number--; // now is 0
  }
  mutex_unlock(&mutex);
}

void write(int id) {
  mutex_lock(&write_reader);

  // write
  printf("write");

  mutex_unlock(&write_reader);
}

int main() {
  SEM_INIT(&reader, 0);
  MUTEX_INIT(&write_reader, 0);
}
