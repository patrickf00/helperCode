#include <stdio.h>
#include <stdlib.h>

int fib(int n);

int main(){
	int n = 13;
	printf("The %d th Fibonacci term is %d\n", n, fib(n-1));
	return 0;
}

// should be called with n-1
int fib(int n){
	// if n <= return n <=> fib(0) returns 0, fib(1) returns 1
	if (n <= 1) return n;
	// where recursion begins, creates long string of recursion
	else return fib(n - 1) + fib(n - 2);
}