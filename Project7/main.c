// 现定义数据结构和全局变量。
#include "conio.c"
#include <stdio.h>
#define M 4
#define N 17
#define Myprintf                                                               \
  printf("|---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--" \
         "-|\n") /*表格控制 */

typedef struct page {
  int num;  /*记录页面号 */
  int time; /*记录调入内存时间 */

} Page; /* 页面逻辑结构，结构为方便算法实现设计 */

Page pages[M];  /*内存单元数 */
int buf[M][N];  /*暂保存内存当前的状态：缓冲区 */
int queue[100]; /*记录调入队列 */
int K;          /*调入队列计数变量 */

//初始化内存单元、缓冲区
void Init(Page *pages, int buf[M][N]) {
  int i, j;
  for (i = 0; i < N; i++) {
    pages[i].num = -1;
    pages[i].time = N - i - 1;
  }
  for (i = 0; i < M; i++)
    for (j = 0; j < N; j++)
      buf[i][j] = -1;
}

//取得在内存中停留最久的页面,默认状态下为最早调入的页面
int GetMax(Page *pages) {
  int i;
  int max = -1;
  int tag = 0;
  for (i = 0; i < M; i++) {
    if (pages[i].time > max) {
      max = pages[i].time;
      tag = i;
    }
  }
  return tag;
}

//判断页面是否已在内存中
int Equation(int fold, Page *pages) {
  int i;
  for (i = 0; i < M; i++)
    if (fold == pages[i].num)
      return i;
  return -1;
}

// LRU算法
void Lru(int fold, Page *pages) {
  int i;
  int val;
  val = Equation(fold, pages);
  if (val >= 0) {
    pages[val].time = 0;
    for (i = 0; i < M; i++)
      if (i != val)
        pages[i].time++;
  } else {
    queue[++K] = fold; /*记录调入页面 */
    val = GetMax(pages);
    pages[val].num = fold;
    pages[val].time = 0;
    for (i = 0; i < M; i++)
      if (i != val)
        pages[i].time++;
  }
}

// FIFO与OPT的算法描述省略。

//主程序
void main() {
  int a[N] = {1, 0, 1, 0, 2, 4, 1, 0, 0, 8, 7, 5, 4, 3, 2, 3, 4};
  int i, j;
start:
  K = -1;
  Init(pages, buf);
  for (i = 0; i < N; i++) {
    Lru(a[i], pages);
    buf[0][i] = a[i];
    /* 记录当前的内存单元中的页面 */
    for (j = 0; j < M; j++)
      buf[j][i] = pages[j].num;
  }
  /*结果输出 */
  printf("内存状态为：\n");
  Myprintf; // 自定义分割符
  for (j = 0; j < N; j++)
    printf("|%2d ", a[j]);
  printf("|\n");
  Myprintf;
  for (i = 0; i < M; i++) { // 将缓冲区的元素打印出来
    for (j = 0; j < N; j++)
      if (buf[i][j] == -1)
        printf("|%2c ", 32); // 空白符
      else
        printf("|%2d ", buf[i][j]);
    printf("|\n");
  }
  Myprintf;
  printf("\n调入队列为:");
  for (i = 0; i < K + 1; i++)
    printf("%3d", queue[i]);
  printf("\n缺页次数为：%6d\n缺页率：%16.6f", K + 1, (float)(K + 1) / N);

  // 重新显示一遍？
  printf("\nAre you continuing!\ty?");
  if (c_getche() == 'y')
    goto start;
}
