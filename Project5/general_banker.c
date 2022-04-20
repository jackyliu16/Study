#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h> 

#include "basic.h"
#include "function.h"
// #define N 100		// the max number of process
// #define M 100		// the max number of source

// init 这个部分采用的方式是预先分配内存空间给一个不定长数组
// https://blog.csdn.net/weixin_42814000/article/details/105205464

// init
int NS=100, NP=100;			// 初始化最大的大小(Number of source, Number of Process);
// 纵向为process， 横向为source
int Max[100][100] = {0};		// 进程总计所需资源
int Available[100] ={0};		// 当前可分配资源
int Need[100][100] = {0};		// 还需要的资源
int Allocation[100][100] = {0};	// 当前占用的资源
int action_process;				// 操作的进程
char str[20];					// 操作的命令
char command[10][20];		

void init(){

	// command
	sprintf(command[0], "quit");		//sprintf 打印到字符串中
	sprintf(command[1], "showdetail");
	sprintf(command[2], "please");
	sprintf(command[3], "help");
	// sprintf(command[3], )
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

void init_tmp(){
	// command
	sprintf(command[0], "quit");		//sprintf 打印到字符串中
	sprintf(command[1], "showdetail");
	sprintf(command[2], "please");
	sprintf(command[3], "help");
}

void showdetail(){
	printf("\nMax: \n");
	for ( int i = 0 ; i < NP ; i++ ) {
		for ( int j = 0 ; j < NS ; j++ ) {
			printf("%d\t", Max[i][j]);
		}
		printf("\n");
	}

	printf("Need: \n");
	for ( int i = 0 ; i < NP ; i++ ) {
		for ( int j = 0 ; j < NS ; j++ ) {
			printf("%d\t", Need[i][j]);
		}
		printf("\n");
	}

	printf("Available: \n");
	for ( int i = 0 ; i < NS ; i++ ) {
		printf("%d\t", Available[i]);
	}

	printf("\nAllocation: \n");
	for ( int i = 0 ; i < NP ; i++ ) {
		for ( int j = 0 ; j < NS ; j++ ) {
			printf("%d\t", Allocation[i][j]);
		}
		printf("\n");
	}

}

/**
 * @brief 对于当前的Allocation进行安全性检查，检查分配完是否会出现死锁
 */
bool security_check(){
	int work[NS], Safety_list[NP];
	int *p = Safety_list;
	bool Finish[NP];
	memset(Finish, false, NP);		
	for ( int i = 0 ; i < NS ; i++ ) {
		work[i] = Available[i];
	}
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
		*(p++) = i;
		goto check_again;

		// 这个地方是想用java的那个continue指定for循环的，但是c不支持
		end_of_check:
	}
	// false if (every one has been check and Still not satisfied) else true
	for ( int i = 0 ; i < NP ;  i++ ) {
		if ( !Finish[i] ) 
			return false;
	}
	printf("安全序列为：");
	p = Safety_list;
	for ( int i = 0 ; i < NP ; i++ ) {
		printf("%d  ", Safety_list[i]);
	}
	return true;
}

void please(int action_process, char *str){
	// test
	int *request;
	request = strtoarray(str);
	for ( int j = 0 ; j < NS ; j++ ) {
		if ( request[j] > Need[action_process][j] ) {
			printf("error ! 134: 您当前申请的资源超过您的最大所需\n");
			showdetail();
			return;
		}
		if ( request[j] > Available[j] ) {
			printf("error ! 135: 您当前申请的资源超过当前可分配资源\n");
			showdetail();
			return;
		}
		// 假意分配
		Available[j] = Available[j] - request[j];
		Allocation[action_process][j] += request[j];
		Need[action_process][j] = Need[action_process][j] - request[j];
	}
	if ( security_check() ) {
		printf("资源申请成功！！！");
		showdetail();
	}
	else {
		printf("资源申请失败！！！");
		for ( int j = 0 ; j < NS ; j++ ) {
			Available[j] += request[j];
			Allocation[action_process][j] -= request[j];
			Need[action_process][j] += request[j];
		}
		showdetail();
	}
}


int main(){
	init();
	// init_tmp();
	showdetail();
	printf("初始化阶段完成，接下来进入标准工作状态：请输入需要申请的进程号\n");
	printf("c:\\>");
	scanf("%d", &action_process);
	while ( action_process != -1 ){
		if ( action_process > NP ) 
			printf("error !");
		else {
			printf("输入进程 %d 所需要的资源数", action_process);
			scanf("%s", str);
			please(action_process, str);
		}
		printf("请输入申请的进程号：");
		scanf("%d",&action_process);


	}
	printf("欢迎下次使用！");

	// process();
	
	// while (strcmp(str, "quit") != 0) {
	// 	printf("\nc:\\>");
	// 	scanf("%s", str);
	// 	process();
	// }

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
1 1,0,2
4 3,3,0
0 0,2,0
*/




