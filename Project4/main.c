#include <stdlib.h>
#include <stdio.h>
#include <time.h>
//#include <dos.h>
#include <string.h>

//定义进程数
#define LEN 10
//定义最高优先级 
#define MAXPIOR 3
// 定义时间片
#define QUANTUM 2
#define PCB sizeof(struct pcb)

struct pcb						//PCB
{
	int ident;					//标识符
	int state;					//状态 0-就绪，1－运行，2－堵塞
	int pior;					//优先级,MAXPIOR为最高优先级*/
	int life;					//生命期*/
	struct pcb *next;			/*指针 */
} *array[MAXPIOR];
// 创建一个 pcb *array[3];

static int idlist[LEN];			/*标识符表 */
int life = 0;					/*总生命期初始化为0 */
char str[20];
char command[7][10];
int killtest = 0;
void init();
int create();
void kill(int x);
void process();
void routine();
void ps();
// other function
int stricmp(const char *str1, const char *str2);

void init()
{
	int i = 0;
	for (i = 0; i < MAXPIOR; i++)
		array[i] = NULL;
	sprintf(command[0], "quit");
	sprintf(command[1], "ps");
	sprintf(command[2], "create");
	sprintf(command[3], "kill");
	sprintf(command[4], "round");
	sprintf(command[5], "sleep");
	sprintf(command[6], "awake");
}

/**
 * 实现随机创建进程的操作
 * 随机优先级，持续时间，顺序进程号
 * 将元素添加到一开始创建的结构体数组中，按照其分属的优先级插入到对应链表中
 */
int create()
{
	int i = 0, pior = 0;
	struct pcb *p, *q, *s;
	while (idlist[i] != 0 && i <= LEN - 1)	// 判断进程是否存在以及进程是否已经使用【如果已经使用，则顺延】
		i++;
	if (i == LEN)
		return -1;
	idlist[i] = 1;
	srand((unsigned) time(NULL));	// 通过一个给出的数字生成一个随机数
	pior = rand() % MAXPIOR;	//最大优先级设定为0－2的整数
	//printf("pior=%d\n",pior);
	s = (struct pcb *) malloc(PCB);	//create a node to keep the process messege
	s->ident = i;
	s->state = 0;
	s->pior = pior;				// 随机指定优先级
	s->life = 1 + rand() % 20;	// 进程有生命期假设为1－20
	s->next = NULL;
	life = life + (s->life);

	p = array[pior];			//建立同优先级队列（链表） 有点不太理解这个地方为什么要这样创建
	/* 对于一开始所创建的结构体数组进行获取，并且将元素插入其中 */

	if (p == NULL)
		array[pior] = s;
	else {
		// 将其添加到同优先级队列的队尾
		while (p != NULL) {
			q = p;
			p = p->next;
		}
		q->next = s;
	}
	printf("success create process id=%d, current process state disp below:\n", s->ident);
	ps();
	//printf("end display\n");
	return 1;
}

void ps()
{
	int i = 0;
	struct pcb *p;
	for (i = 0; i < MAXPIOR; i++) {
		p = array[i];
		while (p != NULL) {
			printf("id:%d,state:%d,pior:%d,life:%d\n", 
			p->ident, p->state, p->pior, p->life);
			p = p->next;
		}
	}
}

/**
 * 从头到尾对于当前存在的结构体进行遍历
 * 并将获取到的结构体编号进行blocked操作，也就是说将线程挂起
 */
void sleep(int x)
{
	int i = 0, test = 0;
	struct pcb *p = NULL, *q = NULL;
	while (test == 0 && i != MAXPIOR) {		// Restrict priority traversal
		p = array[i];
		if (i != MAXPIOR && p == NULL) {	// if this priority is empty
			i++;
			continue;
		}
		while (p != NULL) {					// if this priority wasn't empty
			if (p->ident == x) {
				test = 1;					// if find test
				killtest = 1;				// ?
				break;						// emm...为什么不用goto
			}
			else {
				q = p;
				p = p->next;				// Classical two-pointer Linked-List traversal
			}
		}
		if (test == 0)
			i++;
	}
	
	if (i == MAXPIOR)
		printf("Invaild process number.");
	else if (p->state == 2)
		printf("the process %d has blocked,cannot sleep again!", p->ident);
	else
		p->state = 2;
	// QUESTION:
	// i have not idea's that how this happen ?
	// is it means that sleep == blocked
	ps();
}

/* 基本与sleep相同，不同之处在于将进程置于就绪态 */
void awake(int x)
{
	int i = 0, test = 0;
	struct pcb *p = NULL, *q = NULL;
	while (test == 0 && i != MAXPIOR) {
		p = array[i];
		if (i != MAXPIOR && p == NULL) {
			i++;
			continue;
		}
		while (p != NULL) {
			if (p->ident == x) {
				test = 1;
				killtest = 1;
				break;
			}
			else {
				q = p;
				p = p->next;
			}
		}
		if (test == 0)
			i++;
	}							
	if (i == MAXPIOR)
		printf("Invaild process number.");
	else if (p->state == 0)
		printf("the process %d is ready state,cannot awake again!", p->ident);
	else
		p->state = 0;
	ps();
}

void kill(int x)
{
	int i = 0, test = 0;
	struct pcb *p = NULL, *q = NULL;
	while (test == 0 && i != MAXPIOR) {
		p = array[i];
		if (i != MAXPIOR && p == NULL) {
			i++;
			continue;
		}
		while (p != NULL) {
			if (p->ident == x) {
				test = 1;
				killtest = 1;
				break;
			}
			else {
				q = p;
				p = p->next;
			}
		}
		if (test == 0)
			i++;
	}							/*找到X所在指针 */
	if (i == MAXPIOR)
		printf("Invaild process number.");
	else {
		if (p == array[i]) {		// delete head from wait list
			array[i] = array[i]->next;
			idlist[x] = 0;
			free(p);
		}
		else {						
			q->next = p->next;		// delete node[q->next == p]
			idlist[x] = 0;
			life = life - (p->life);// ??? 这个总生命期的概念是否相当于这个程序的总生命周期
			free(p);
		}
	}
}

void process()					//对输入命令的处理
{
	int i = 0, ii = 0;
	for (i = 0; i < 7; i++)		
		if (stricmp(str, command[i]) == 0)
			break;
	// Implement matching based on for
	switch (i) {
	case 0:
		printf("thank you for using the program!\n");
		exit(0);
		break;
	case 1:
		ps();
		break;
	case 2:
		create();
		break;
	case 3:
		{
			printf("Which process you want to kill?\n");
			scanf("%d", &ii);
			kill(ii);
			break;
		}
	case 4:
		routine();
		break;
	case 5:
		printf("Which process you want to sleep?\n");
		scanf("%d", &ii);
		sleep(ii);
		break;
	case 6:
		printf("Which process you want to awake?\n");
		scanf("%d", &ii);
		awake(ii);
		break;
	default:
		printf("Error command.Please input create, ps, round, kill, sleep, awake, quit\n");
	}
}

void routine()					//执行一次调度运行，将最高优先级队列的进程运行1个时间片，并降低其优先级
{
	int i = MAXPIOR - 1, pior = 0, t;
	struct pcb *pp, *qq, *pr, *r;
	do {
		while (i >= 0 && array[i] == NULL)
			i = i--;
		if (i < 0) {
			printf("NO process,please create it! \n");
			return;
		}
		pr = r = array[i];
		while (r != NULL && r->state != 0) {
			pr = r;
			r = r->next;
		}
		i--;
	}
	while (r == NULL);
	//从高优先队列中寻找就绪进程以调度它
	printf("The one in the hightest piror process will execute 1 quantum.\n");
	r->state = 1;				//进程处于运行状态
	printf("process id=%d is running...", r->ident);
	for (int k = 1; k < 600000; k++)
		for (int k1 = 1; k1 < 1000; k1++);	//延时
	printf("end,change to ready state\n");
	r->pior = (r->pior) / 2;
	r->state = 0;				//进程处于就绪状态
	if (r->life - QUANTUM > 0) {
		r->life = r->life - QUANTUM;	//时间减少QUANTUM
		life = life - QUANTUM;
	}
	else {
		life = life - r->life;
		r->life = 0;
	}

	if (r->life == 0)			//进程运行完成，KILL它
	{
		printf("the process %d is successful run,and release it!\n", r->ident);
		kill(r->ident);
	}
	else {
		if (pr == r)			//将r结点从原队列中删除
			array[i + 1] = r->next;
		else
			pr->next = r->next;

		t = r->pior;			//将r进程加入到相应低优先级队列中的最后
		pp = array[t];
		qq = NULL;
		while (pp != NULL) {
			qq = pp;
			pp = pp->next;
		}
		if (qq == NULL)			//插入到队尾
			array[t] = r;
		else
			qq->next = r;
		r->next = NULL;
	}

	printf("after...\n");
	ps();
	printf("\n 1 quantum successful run!\n");
}

//**********************************
int main()
{
	init();
	printf
		("Welcome to the Process Scheduling system. This program simulate the Round-Robin with piror Scheduling alogrithm. \n");
	printf("c:\\>");
	scanf("%s", str);
	process();

	while (strcmp(str, "quit") != 0) {
		printf("\nc:\\>");
		scanf("%s", str);
		process();
	}

	return 0;
}


/* ---------- Other Function ---------- */
/* 实现两个字符串的对比，并且忽略大小写 
这个的存在是为了填补stricmp函数的缺失 我的gnu版本中不支持该函数[似乎只在msvc里面支持，并已经被弃用] */
int stricmp(const char *str1, const char *str2)
{
	int i, j = 0;
	for (i = 0; str1[i] != '\0'; i++);
	for (j = 0; str2[j] != '\0'; j++);
	if (i == j || i > j) {
		i = 0;
		j = 0;
		for (i = 0; str1[i] != '\0'; i++) {
			if (str1[i] - str2[j] == 32 || str1[i] - str2[j] == -32 || str1[i] - str2[j] == 0) {
				j++;
			}
			else if (str1[i] < str2[j]) {
				// str1 less than str2
				return -1;
			}
			else {
				// str1 greater than str2
				return 1;
			}
		}
	}
	else {
		i = 0;
		j = 0;
		for (i = 0; str2[i] != '\0'; i++) {
			if (str1[i] - str2[j] == 32 || str1[i] - str2[j] == -32 || str1[i] - str2[j] == 0) {
				j++;
			}
			else if (str1[i] < str2[j]) {
				// str1 less than str2
				return -1;
			}
			else {
				// str1 greater than str2
				return 1;
			}
		}
	}
	return 0;
}
