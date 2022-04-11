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

struct pcb  //PCB
{	
	int ident;//标识符
	int state;//状态 0-就绪，1－运行，2－堵塞
	int pior;//优先级,MAXPIOR为最高优先级*/
	int life;//生命期*/
	struct pcb *next;/*指针*/
} *array[MAXPIOR];

static int idlist[LEN];/*标识符表*/
int life=0;/*总生命期初始化为0*/
char str[20];
char command[7][10];
int killtest=0;
void init();
int create();
void kill(int x);
void process();
void routine();
void ps();

void init()
{
	int i=0;
	for (i=0;i<MAXPIOR;i++)
	array[i]=NULL;
	sprintf(command[0],"quit");
	sprintf(command[1],"ps");
	sprintf(command[2],"create");
	sprintf(command[3],"kill");
	sprintf(command[4],"round");
	sprintf(command[5],"sleep"); 
	sprintf(command[6],"awake");
}

int create()
{
	int i=0,pior=0;
	struct pcb *p,*q,*s;
	while (idlist[i]!=0&&i<=LEN-1)
		i++;
	if (i==LEN) 
		return -1;
	idlist[i]=1;
	srand((unsigned)time(NULL));   
	pior=rand()%MAXPIOR;    //最大优先级设定为0－2的整数
	//printf("pior=%d\n",pior);
	s=(struct pcb *)malloc(PCB);//create a node to keep the process messege
	s->ident=i;
	s->state=0;
	s->pior=pior;
	s->life=1+rand()%20;//进程有生命期假设为1－20
	s->next=NULL;
	life=life+(s->life);

	p=array[pior];//建立同优先级队列（链表）
	if (p==NULL)
		array[pior]=s;
	else 
	{
		while(p!=NULL)
		{
			q=p;
			p=p->next;
		}
		q->next=s;
	}
	printf("success create process id=%d, current process state disp below:\n",s->ident);
	ps();
	//printf("end display\n");
	return 1;
}

void ps()
{	
	int i=0;
 	struct pcb *p;
	for (i=0;i<MAXPIOR;i++)
		{
			p=array[i];
			while (p!=NULL)
			{
				printf("id:%d,state:%d,pior:%d,life:%d\n",p->ident,p->state,p->pior,p->life);
				p=p->next;
			}
		}
}

void sleep(int x)
{
	int i=0,test=0;
	struct pcb *p=NULL,*q=NULL;
	while(test==0&&i!=MAXPIOR)
	{
		p=array[i];
		if (i!=MAXPIOR && p==NULL)
		{
			i++;continue;
		}
		while(p!=NULL)
		{
			if (p->ident==x) 
			{
				test=1;killtest=1;break;
			}
			else 
			{
				q=p;p=p->next;
			}
		}
		if (test==0) 
			i++;
	}
	/*找到X所在指针*/
	if (i==MAXPIOR) 
		printf("Invaild process number.");
	else
		if (p->state==2)
			printf("the process %d has blocked,cannot sleep again!",p->ident);
		else
			p->state=2;
	ps();
}

void awake(int x)
{
	int i=0,test=0;
	struct pcb *p=NULL,*q=NULL;
	while(test==0&&i!=MAXPIOR)
	{
		p=array[i];
		if (i!=MAXPIOR && p==NULL)
		{
			i++;
			continue;
		}
		while(p!=NULL)
		{
			if (p->ident==x) 
			{
				test=1;killtest=1;break;
			}
			else 
			{
				q=p;p=p->next;
			}
		}
		if (test==0) 
			i++;
	}/*找到X所在指针*/
	if (i==MAXPIOR) 
		printf("Invaild process number.");
	else
		if (p->state==0)
			printf("the process %d is ready state,cannot awake again!",p->ident);
		else
			p->state=0;
	ps();
}

void kill(int x)
{
	int i=0,test=0;
	struct pcb *p=NULL,*q=NULL;
	while(test==0&&i!=MAXPIOR)
	{
		p=array[i];
		if (i!=MAXPIOR && p==NULL)
		{
			i++;
			continue;
		}
		while(p!=NULL)
		{
			if (p->ident==x) 
			{
				test=1;
				killtest=1;
				break;
			}
			else 
			{
				q=p;
				p=p->next;
			}
		}
		if (test==0) 
			i++;
	}/*找到X所在指针*/
	if (i==MAXPIOR) 
		printf("Invaild process number.");
	else 
	{
		if (p==array[i]) 
		{
			array[i]=array[i]->next;
			idlist[x]=0;  
			free(p);
		}
		else
		{
			q->next=p->next;
			idlist[x]=0;
			life=life-(p->life);
			free(p);
		} 
	}
}

void process()//对输入命令的处理
{
	int i=0,ii=0;
	for (i=0;i<7;i++)
		if ( stricmp(str,command[i]) ==0)
			break;
	switch(i)
	{
		case 0:
			printf("thank you for using the program!\n");
			exit(0);
			break;
		case 1:
			ps();break;
		case 2:
			create();break;
		case 3:
		{
			printf("Which process you want to kill?\n");
			scanf("%d",&ii);
			kill(ii);
			break;
		}
		case 4:
			routine();break;
		case 5:
			printf("Which process you want to sleep?\n");
			scanf("%d",&ii);
			sleep(ii);break;
		case 6:
			printf("Which process you want to awake?\n");
			scanf("%d",&ii);
			awake(ii);break;
		default:
			printf("Error command.Please input create, ps, kill,sleep,awake,quit\n"); 
	}
}

void routine()//执行一次调度运行，将最高优先级队列的进程运行1个时间片，并降低其优先级
{
	int i=MAXPIOR-1,pior=0,t;
	struct pcb *pp,*qq,*pr,*r;
	do {
		while (i>=0 && array[i]==NULL)
			i=i--;
		if (i<0)
		{
			printf("NO process,please create it! \n");
			return ;
		}
		pr=r=array[i];
		while (r!=NULL && r->state!=0) 
			{pr=r;r=r->next;}
		i--;
	}
	while(r==NULL);
	//从高优先队列中寻找就绪进程以调度它
	printf("The one in the hightest piror process will execute 1 quantum.\n");
	r->state=1;    //进程处于运行状态
	printf("process id=%d is running...",r->ident);
	for (int k=1;k<600000;k++)
		for(int k1=1;k1<1000;k1++);      //延时
	printf("end,change to ready state\n");
	r->pior=(r->pior)/2;
	r->state=0;    //进程处于就绪状态
	if(r->life-QUANTUM>0)
	{
		r->life=r->life-QUANTUM; //时间减少QUANTUM
		life=life-QUANTUM;
	}
	else
	{
		life=life-r->life;
		r->life=0;
	}

	if (r->life==0)//进程运行完成，KILL它
	{
		printf("the process %d is successful run,and release it!\n",r->ident);
		kill(r->ident);
	}
	else
	{
		if (pr==r)   //将r结点从原队列中删除
			array[i+1]=r->next;
		else
			pr->next=r->next;

		t=r->pior; //将r进程加入到相应低优先级队列中的最后
		pp=array[t];
		qq=NULL;
		while (pp!=NULL)
		{
			qq=pp;pp=pp->next;
		}
		if(qq==NULL)     //插入到队尾
			array[t]=r;
		else
			qq->next=r; 
		r->next=NULL;
	}

	printf("after...\n"); 
	ps();
	printf("\n 1 quantum successful run!\n");
}

//**********************************
int main()
{
	init();
	printf("Welcome to the Process Scheduling system. This program simulate the Round-Robin with piror Scheduling alogrithm. \n");
	printf("c:\\>");
	scanf("%s",str);
	process();

	while (strcmp(str,"quit")!=0)
	{
		printf("\nc:\\>");
		scanf("%s",str);
		process();
	}

	return 0;
}
