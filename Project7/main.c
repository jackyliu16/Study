// 现定义数据结构和全局变量。
#include "conio.c"
#include <stdio.h>
#define M 4
#define N 12
#define Myprintf                                                               \
  printf("|---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--" \
         "-|\n")				/*表格控制 */

typedef struct page {
	int num;					/*记录页面号 */
	int time;					/*记录调入内存时间[FIFO]/记录闲置时间[LRU] */
} Page;							/* 页面逻辑结构，结构为方便算法实现设计 */
int a[N] = {1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5};	
Page pages[M];					/*内存单元数 */
int buf[M][N];					/*暂保存内存当前的状态：缓冲区 */
					/*保存页面的使用顺序*/
int queue[100];					/*记录调入队列 */
int K;							/*调入队列计数变量[或者说是缺页中断次数] */

//初始化内存单元、缓冲区
void Init(Page * pPages, int buf[M][N])
{
	int i, j;
	for (i = 0; i < N; i++) {
		pPages[i].num = -1;
		pPages[i].time = N - i - 1;
	}
	for (i = 0; i < M; i++)
		for (j = 0; j < N; j++)
			buf[i][j] = -1;
}

// 取得 pages 中 time 最大的页面的页面号
int GetMax(Page * pages)
{
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

int HowLongAfterItWillBeUsed(int fold, int times, Page *pages){
	int page_num = -1;
	int max_value = -1;
	for ( int i = 0 ; i < M ; i++ ) {
		// for each item in pages[]
		// find how many times it will been used
		int j;
		for ( j = times + 1 ; j < N && a[j] != pages[i].num; j++ ) 
			; 
		if ( j - times > max_value ) {
			page_num = i;
			max_value = j - times;
		}
		else {
			;
		}
	}
	return page_num;
}


//判断页面是否已在内存中[传入页面号]
int Equation(int fold, Page * pPages)
{
	int i;
	for (i = 0; i < M; i++)
		if (fold == pPages[i].num)
			return i;
	return -1;
}

// LRU算法
void Lru(int fold, Page * pages)
{
	int i;
	int val;							
	val = Equation(fold, pages);
	if (val >= 0) {
		pages[val].time = 0;
		for (i = 0; i < M; i++)			// for other pages, they all wait for a time slice
			if (i != val)
				pages[i].time++;
	}
	else {
		queue[++K] = fold;				/*记录调入页面 */
		val = GetMax(pages);
		pages[val].num = fold;
		pages[val].time = 0;
		for (i = 0; i < M; i++)			// for other pages, they all wait for a time slice
			if (i != val)
				pages[i].time++;
	}
}

// FIFO与OPT的算法描述省略。

void FIFO(int fold, Page * pages){
	int ret = Equation(fold, pages);
	if ( ret >= 0 ) {
		// all pages time add
		for ( int i = 0 ; i < M ; i ++ ) 
			pages[i].time++;
	}
	else {
		// core load 
		queue[++K] = fold;
		ret = GetMax(pages);			// 停留最久的元素time最大
		pages[ret].num = fold;
		pages[ret].time = 0;
		for ( int i = 0 ; i < M ; i++ )	// 认为一旦被引入，则可以认为当前时间为1
			pages[i].time++;
	}
}

void OPT(int fold, Page * pages, int times)
{
	int ret = Equation(fold, pages);
	if ( ret >= 0 ) {
		;
	}
	else {
		// first check if have some page is empty
		queue[++K] = fold;
		ret = -1;
		for ( int i = 0 ; i < M ; i++ ) {
			if (pages[i].num == -1){
				ret = i;
				goto change_of_OPT;
			}
		}
		// from pages list and a[] find the page number who has the maximum time to access
		ret = HowLongAfterItWillBeUsed(fold, times, pages);

	  change_of_OPT:
	  	pages[ret].num = fold;
		pages[ret].time = 0;
	}
}


//主程序
void main()
{
	// int a[N] = { 1, 0, 1, 0, 2, 4, 1, 0, 0, 8, 7, 5, 4, 3, 2, 3, 4 }; //Page use queue
	// a = ; 
	int i, j;
  start:
	K = -1;
	Init(pages, buf);
	for (i = 0; i < N; i++) {
		OPT(a[i], pages, i);
		buf[0][i] = a[i];
		/* 记录当前的内存单元中的页面 */
		for (j = 0; j < M; j++)
			buf[j][i] = pages[j].num;
	}
	/*结果输出 */
	printf("内存状态为：\n");
	Myprintf;					// 自定义分割符
	for (j = 0; j < N; j++)
		printf("|%2d ", a[j]);
	printf("|\n");
	Myprintf;
	for (i = 0; i < M; i++) {	// 将缓冲区的元素打印出来
		for (j = 0; j < N; j++)
			if (buf[i][j] == -1)
				printf("|%2c ", 32);	// 空白符
			else
				printf("|%2d ", buf[i][j]);
		printf("|\n");
	}
	Myprintf;
	printf("\n调入队列为:");
	for (i = 0; i < K + 1; i++)
		printf("%3d", queue[i]);
	printf("\n缺页次数为：%6d\n缺页率：%16.6f", K + 1, (float) (K + 1) / N);

	// 重新显示一遍？
	printf("\nAre you continuing!\ty?");
	if (c_getche() == 'y')
		goto start;
}
