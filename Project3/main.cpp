#inlude "basic.h"
 
semphore sem[5]; 	//deinfe 5 semphores
pnode * pr[20]; 	//define 0-19 total 20 process
//down operation 

 void down(char * sname,int pid) 
{ 
	int fflag,pflag; 
	pnode *p,*p1; 
	semphore *s;  
	fflag=0; 
	pflag=0; 
	int i;
	
	for(i=0;i<5;i++)
		if(!strcmp(sem[i].name,sname))//find semaphore by name 
		{ 
			s=&sem[i]; 
			fflag=1; 
			break; 	
		} 
	for(i=0;i<20;i++)   //find pcb by pid 
		if(pr[i]->node->pid == pid) 	
		{ 
			p1 = pr[i];     
			pflag=1; 
			break; 
		} 
	if(!fflag)  //semaphore is not exist 
	{ 
		printf("the semphore '%s' is not exist!\n",sname); 
		return; 
	} 
	if(!pflag)  //pid is not exist 
	{ 
		printf("the process '%d' is not exist!\n",pid); 
		return; 
	} 
	s->count--;   					//semaphore! s value -1
	if(s->count>=0) //this pcb get the semaphore 如果当前进程没有运行完 
		s->curpid = p1->node->pid; 	// 设定当前信号量对饮的进程号 
	else 
	{ 
	// 如果当前进程的信号量降为0，则从等待队列中寻求下一个元素 ？？？ 
		if(s->wlist)  //the link is not NULL, add the pcb to the last 
	    { 
			for(p=s->wlist;p->next;p=p->next);   
			p->next=p1; 
		}  
		else  //this pcb is the first pcb be added to the down list 
		    s->wlist=p1; 
	} 
} 
 
//up operation 
void up(char *sname) 
{ 
	int fflag=0; 
	for(int i=0;i<5;i++) {
	
		if(!strcmp(sem[i].name,sname)) //find the semaphore by name 
		{ 
			fflag=1; 
			break; 
		} 
		if(fflag)  //find it 
		{ 
			sem[i].count++; 
			if(sem[i].wlist)  //there are processes in the down list 
			{ 
				sem[i].curpid = sem[i].wlist->node->pid; 
				sem[i].wlist = sem[i].wlist->next; 
			} 
		} 
		else
		 	printf("the semphore '%s' is not exist!\n",sname); 
	}
} 

//show semphore infomation 
void showdetail() 
{ 
	int i; 
	pnode *p; 
	printf("\n"); 
	// 遍历五个信号 - 逐一输出他们的 
	for(i=0;i<5;i++)  
	{ 
		// 有点不太理解这个计数值是干嘛用的，大体上是类似于之前的那个showdetail 
		if(sem[i].count<=0) 
		{ 
			printf("%s (current_process  %d):  ",sem[i].name,sem[i].curpid); 
			p=sem[i].wlist; 	
			while(p)
			{ 
				printf("%5d",p->node->pid); 
				p=p->next; 
			} 
		} 
		else // 如果当前semphore不存在挂载的进程 
			printf("%s :  ",sem[i].name); 
		printf("\n"); 
	} 
} 
 
/***************************************************************/ 
// init semphore and process array 
void init() 
{ 
	//init semaphore 
	strcat(sem[0].name,"s0"); 
	strcat(sem[1].name,"s1"); 
	strcat(sem[2].name,"s2"); 
	strcat(sem[3].name,"s3"); 
	strcat(sem[4].name,"s4"); 
	// 对于 semaphore 进行逐步初始化 
	for(int i=0;i<5;i++) 
	{ 
		sem[i].wlist=NULL; 
		sem[i].count=1; 
	} 
	//init process 初始化20个进程，但是我不太理解这个为啥要这样搞 
	for(int i=0;i<20;i++) 
	{ 
		pr[i] = new pnode;
		pr[i]->node=new pcb; 
		pr[i]->node->pid=i; 
		pr[i]->brother=NULL; 
		pr[i]->next=NULL; 
		pr[i]->sub=NULL; 
	} 
} 
 
int main() 
{ 
	short cflag,pflag; 
	char cmdstr[32]; 
	char *s,*s1,*s2; 
	
	initerror(); 
	init(); 
	
	for(;;) 
	{ 
		cflag=0; 
		pflag=0; 
		printf("cmd:"); 
		scanf("%s",cmdstr); 
		if(!strcmp(cmdstr,"exit"))  //exit the program 
		break; 
		if(!strcmp(cmdstr,"showdetail")) 
		{ 
			cflag = 1; 
			pflag = 1; 
			showdetail(); 
		} 
		else 
		{ 
			s = strstr(cmdstr,"down"); 	//create process 
			if(s) 
			{ 
				cflag=1; 
				//get parameter 
				s1 = substr(s,instr(s,'(')+1,instr(s,',')-1); 
				s2 = substr(s,instr(s,',')+1,instr(s,')')-1); 
				if(s1 && s2) 			// 如果二者非空 
				{ 
					down(s1,atoi(s2)); 	// atoi: 丢弃任何空白字符 
					pflag=1; 
				} 
			} 
			else 
			{ 
				s=strstr(cmdstr,"up");	//delete process 
				if(s) 
				{ 
					cflag=1; 
					s1 = substr(s,instr(s,'(')+1,instr(s,')')-1); 
					if(s1) 
					{ 
						up(s1); 
						pflag=1; 
					} 
				} 
			} 
		} 
		if(!cflag) 
			geterror(0); 
		else if(!pflag) 
			geterror(1);   
		} 
	return 0;
} 

