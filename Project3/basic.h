#ifndef basic_h
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define basic_h
char *errormsg[256];
//process control block

struct pcb
{
	int pid;//process id
	int ppid;//parent process id
	int prio;//priority
	int state;//state
	int lasttime;//last execute time
	int tottime; //totle execute time
};

//process node
struct pnode
{
	pcb *node;
	pnode *sub;			// 子节点 ？ 
	pnode *brother;		// 兄弟节点  
	pnode *next;		// 实现就绪链表 
};

//信号量 - 我有点不太理解为什么这个部分不使用typedef struct 的方案，同时还在正文中没有使用结构体的方案进行引用 
struct semphore{
	char name[5];		//名称
	int count;			//计数值
	int curpid;			//当前进程 id
	pnode *wlist; 		//等待链表	用于链接所有等待该资源的进程
};
#define geterror(eno) printf("%s\n",errormsg[eno])

void initerror()
{
	errormsg[0] = (char *)malloc(20);
	errormsg[0]="error command!";
	errormsg[1] = (char *)malloc(20);
	errormsg[1]="error parameter!";
	errormsg[2]=(char *)malloc(20);
	errormsg[2]="can't find pid!";
	errormsg[3]=(char *)malloc(20);
	errormsg[3]="can't find ppid!";
	errormsg[4]=(char *)malloc(20);
	errormsg[4]="pid is already exist";
}

//get a substring in string s
char * substr(char *s,int start,int end)
{
	char *s1;
	int i;
	int len = strlen(s);
	if(start<0 || end>=len || start>end)
        return NULL;
	s1=(char *)malloc(end-start+2);
	for(i=0;i<=end-start;i++)
        s1[i] = s[i+start];
	s1[i]='\0';
	return s1;
}
//find the location of c in string s
int instr(char *s,char c)
{
	unsigned i;
	for(i=0;i<strlen(s);i++)
		if(s[i]==c)
            return i;
	return -1;
}
//change the string to array data
int * strtoarray(char *s)
{
	int *a,count,x1;
	unsigned int i;
	char c, *s1,*s2;
	if(!s)
	{
		printf("string can't be null!\n");
		return NULL;
	}
	count=0;
	s1=s;
	for(i=0;i<strlen(s1);i++)
		if(s1[i]==',')
            count++;
	count++;
	a = (int *)malloc(count);
	c=',';
	for(i=0;i < count;i++)
	{
		x1 = instr(s1,c);
		if(x1>=0)
            s2=substr(s1,0,x1-1);
		else
            s2=s1;
		a[i]=atoi(s2);
		if(c==',')
            s1=substr(s1,x1+1,strlen(s1)-1);
	}
	return a;
}
#endif
