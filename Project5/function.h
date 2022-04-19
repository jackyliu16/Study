#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h> 

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


// static char * left_subString(char *dest, const char *src, int n){
// 	char *p = dest;
// 	int len = strlen(src);

// 	if ( n > len ) {
// 		n = len;
// 	}

// 	while ( n-- ) 
// 		*(p++) = *(src++);
// 	*(p++) = '\0';

// 	return dest;
// }

// /**
// 传入并返回一个指针，该该指针节选src的 [start, end) 的字符串
// */
// static char *subString(char *dest, const char *src, int start, int end){
// 	char *p = dest;
// 	int len = strlen(src);
// 	int count = 0;

// 	if ( end > len ) {
// 		end = len;
// 	}

// 	for ( int i = 0 ; i < start ; i++ ) src++;

// 	while ( start != end ) {
// 		*(dest++) = *(src++);
// 		start++;
// 	}
// 	*(dest++) = '\0';
// 	// return the first pointer
// 	return dest;
// }





// 垃圾堆

// void please(int split){
// 	// try to match
// 	char * p = str;
// 	while ( split -- > -1 ) p++;
// 	int *request = strtoarray(p);

// 	for ( int i = 0 ; i < 3 ; i++ ) {
// 		printf("%d\t", request[i]);
// 	}

// 	int flag = 0;
	
	
// 	end_of_for_please:
// 	if ( flag == -1 ) 
// 		printf("you ask for too much");


// 	return;
// }




// void process(){
// 	// find
// 	int i,ii;
// 	char *command_input;
// 	for ( i = 0 ; str[i] != '\0' ; i++ ) {
// 		// TODO 不知道为什么没有办法识别（ complete
// 		if ( str[i] == '(' || str[i] == ' ' )
// 			break;
// 	}

// 	command_input = substr(str, 0, i-1);
// 	for ( ii = 0 ; ii < 10; ii++ ) {
// 		if (stricmp(command_input, command[ii]) == 0 )
// 			break;
// 	}
// 	printf("split: %d", ii);
// 	switch (ii) {
// 		case 0:
// 			printf("thanks for using!");
// 			exit(0);
// 			break;
// 		case 1:
// 			showdetail();
// 			break;
// 		case 2:
// 			please(i);
// 			break;
// 		case 3:
// 			printf("help:\n");
// 			printf("you can using quit, showdetail, please, help");
// 			break;
// 		default:
// 			printf("error command!\nyou could use help to find the command.\n");


// 	}

// 	free(command_input);
// }