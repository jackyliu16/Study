#include <string.h>
#include <stdio.h>

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


int main(){
    char dest[20];
    char src[20];
	scanf("%s", src);

	

    // subString(dest, src, 2, 5);

    printf("%s", dest);
}

