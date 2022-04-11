#include "basic.h"
pnode *proot;					//system process tree root
pnode *plink;					//system process link head
//create process
int createpc(int *para)
{
	//add your code here
	pnode *p, *p1, *pp;
	int pflag;
	pflag = 0;
	for (p = plink; p; p = p->next) {
		if (p->node->pid == para[0])	//check if this pid is already exist
		{
			printf("pid %d is already exist!\n", para[0]);
			return -1;
		}
		if (p->node->pid == para[1])	//find parent pcb
		{
			pflag = 1;
			pp = p;
		}
	}
	if (!pflag) {
		printf("parent id %d is not exist!\n", para[1]);
		return -2;
	}
//init new pcb
	p1 = new pnode;
	p1->node = new pcb;
	p1->node->pid = para[0];
	p1->node->ppid = para[1];
	p1->node->prio = para[2];
	p1->sub = NULL;
	p1->next = NULL;
	p1->brother = NULL;
//add to process tree
	if (!pp->sub)
		pp->sub = p1;
	else {
		for (p = pp->sub; p->brother; p = p->brother);
		p->brother = p1;
	}
// add to process link
	for (p = plink; p->next; p = p->next);
	p->next = p1;
	return 0;
}

//show process detail
void showdetail()
{
	//add your code here
	pnode *p, *p1;
	p = plink;
	for (; p;)					//print all pcb info
	{
		printf("%d(prio %d):", p->node->pid, p->node->prio);
		p1 = p->sub;
		for (; p1;)				//print sub pcb
		{
			printf("%d(prio %d)", p1->node->pid, p1->node->prio);
			p1 = p1->brother;
		}
		printf("\n");
		p = p->next;
	}
	printf("\n");
}

//don't change
int main()
{
	initerror();
	short cflag, pflag;
	char cmdstr[32];
	proot = new pnode;
	proot->node = new pcb;
	proot->node->pid = 0;
	proot->node->ppid = -1;
	proot->node->prio = 0;
	proot->next = NULL;
	proot->sub = NULL;
	proot->brother = NULL;
	plink = proot;
	for (;;) {
		cflag = 0;
		pflag = 0;
		printf("cmd:");
		scanf("%s", cmdstr);
		if (!strcmp(cmdstr, "exit"))	//exit the program
			break;
		if (!strcmp(cmdstr, "showdetail")) {
			cflag = 1;
			pflag = 1;
			showdetail();
		}
		else {
			int *para;
			char *s, *s1;
			s = strstr(cmdstr, "createpc");	//create process
			if (s) {
				cflag = 1;
				para = (int *) malloc(3);
				//getparameter
				s1 = substr(s, instr(s, '(') + 1, strlen(s) - 2);	//get param string
				para = strtoarray(s1);	//get parameter
				createpc(para);	//create process
				pflag = 1;
			}
		}
		if (!cflag)
			geterror(0);
		else if (!pflag)
			geterror(1);
	}
}
