#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define SIZE 20
long str2long(char *str)
{
	long ret = 0;

	for(int i=0;i<strlen(str);i++)
	{
		if(str[i]>='0' && str[i]<='9')
		{
			ret = ret * 10 + str[i]-'0';
		}
	}
	
	return str[0]=='-' ? -ret : ret;
}



int main()
{
    char A[SIZE], B[SIZE];
    long a, b;
    
    while(scanf("%s %s", &A, &B) != EOF)
    {
		a = b = 0;
		a = str2long(A);
		b = str2long(B);
		printf("%lld\n", a + b);

    }
    return 0;
}
