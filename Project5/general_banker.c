#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h> 
// #define N 100		// the max number of process
// #define M 100		// the max number of source

// init 这个部分采用的方式是预先分配内存空间给一个不定长数组
// https://blog.csdn.net/weixin_42814000/article/details/105205464

// init
int NS=100, NP=100;			// 初始化最大的大小(Number of source, Number of Process);
// 纵向为process， 横向为source
int Max[100][100] = {0};
int Available[100] ={0};
int Need[100][100] = {0};
int Allocation[100][100] = {0};

void init(){
		// int tmp;
	// printf("请输入资源的种类：");
	// scanf("%d", &tmp);
	// if ( tmp > NS ) {
	// 	printf("你所申请的资源数量过多(只能申请100以内)\n");
	// 	exit(0);
	// }
	// NS = tmp;
	// printf("请输入进程的数量：");
	// scanf("%d", &tmp);
	// if ( tmp > NP ) {
	// 	printf("你所申请的进程数量过多(只能申请100以内)\n");
	// 	exit(0);
	// }
	// NP = tmp;
	
	//--------------------//
	NS = 3, NP = 5;
	int tmp;
	//--------------------//

	// printf("请逐一输入Avaliable矩阵:");
	// for ( int j = 0 ; j < NS ; j++ ) {
	// 	scanf("%d", &tmp);
	// 	Available[j] = tmp;
	// }
	// printf("请逐一输入Max矩阵:");
	// for ( int i = 0 ; i < NP ; i++ ) {
	// 	for ( int j = 0 ; j < NS ; j++ ) {
	// 		scanf("%d", &tmp);
	// 		Max[i][j] = tmp;
	// 	}
	// }
	// printf("请逐一输入Allocation矩阵:");
	// for ( int i = 0 ; i < NP ; i++ ) {
	// 	for ( int j = 0 ; j < NS ; j++ ) {
	// 		scanf("%d", &tmp);
	// 		Allocation[i][j] = tmp;
	// 	}
	// }
	// printf("请逐一输入Need矩阵:");
	// for ( int i = 0 ; i < NP ; i++ ) {
	// 	for ( int j = 0 ; j < NS ; j++ ) {
	// 		scanf("%d", &tmp);
	// 		Need[i][j] = tmp;
	// 	}
	// }

	printf("究极偷懒秘诀：");
	for ( int j = 0 ; j < NS ; j++ ) {
		scanf("%d", &tmp);
		Available[j] = tmp;
	}
	for ( int i = 0 ; i < NP ; i++ ) {
		for ( int j = 0 ; j < NS ; j++ ) {
			scanf("%d", &tmp);
			Max[i][j] = tmp;
		}
	}
	for ( int i = 0 ; i < NP ; i++ ) {
		for ( int j = 0 ; j < NS ; j++ ) {
			scanf("%d", &tmp);
			Allocation[i][j] = tmp;
		}
	}
	for ( int i = 0 ; i < NP ; i++ ) {
		for ( int j = 0 ; j < NS ; j++ ) {
			scanf("%d", &tmp);
			Need[i][j] = tmp;
		}
	}
}


/**
 * @brief 对于当前的Allocation进行安全性检查，检查分配完是否会出现死锁
 */
bool security_check(){
	int work[NS];
	for ( int i = 0 ; i < NS ; i++ ) {
		work[i] = Available[i];
	}
	bool Finish[NP];
	memset(Finish, false, NP);		
	// void *memset(void *str, int c, size_t n) 复制字符 c（一个无符号字符）到参数 str 所指向的字符串的前 n 个字符

	check_again:
	for ( int i = 0 ; i < NP ; i++ ) {
		// skep this process
		if ( Finish[i] ) 
			continue;
		// check this process if could been finish
		for ( int j = 0 ; j < NS ; j++ ) { 
			if ( Need[i][j] > work[j] ) 
				goto end_of_check;
		}
		// 实际发生调度行为，配给资源，并且释放该进程当前占用的资源
		// before this action, may be the process has been check could finish, so we check again;
		for ( int j = 0 ; j < NS ; j++ ) {
			work[j] += Allocation[i][j];
			Finish[i] = true;
		}
		goto check_again;

		end_of_check:
		// 这个地方是想用java的那个continue指定for循环的，但是c不支持
	}
	// false if (every one has been check and Still not satisfied) else true
	for ( int i = 0 ; i < NP ;  i++ ) {
		if ( !Finish[i] ) 
			return false;
	}
	return true;
}



int main(){
	init();

	return 0;
}
/* 测试样例
3
5
3 3 2
7 5 3 3 2 2 9 0 2 2 2 2 4 3 3
0 1 0 2 0 0 3 0 2 2 1 1 0 0 2
7 4 3 1 2 2 6 0 0 0 1 1 4 3 1
*/
/* 究极偷懒秘诀：
3 3 2 7 5 3 3 2 2 9 0 2 2 2 2 4 3 3 0 1 0 2 0 0 3 0 2 2 1 1 0 0 2 7 4 3 1 2 2 6 0 0 0 1 1 4 3 1
*/
