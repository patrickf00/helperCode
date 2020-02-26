#include <stdio.h>
#include <stdlib.h>

int recursiveBinarySearch();

int main(){
	int const ARRSIZE = 8;
	int intarr[ARRSIZE], target, i, left, right, mid;  
	printf("Please input %d integers which are sorted in the ascending order and a target value.", ARRSIZE);   
	for(i= 0; i<ARRSIZE; i++){ 
		scanf("%d", &intarr[i]); 
	} 
	printf("\nPlease enter a number to find.");
	scanf("%d", &target);
	// left boundry
	left = 0; 
	// right boundry
	right = ARRSIZE-1;
	// run until left boundry is greater than right boundry 
	while(left <= right){ 
		// mid is floor of average of left and right boundry
		mid = (left+right)/2; 
		// found, break loop
		if(intarr[mid] == target){ 
			printf("The index of the target in the array is %d.\n", mid); 
			break; 
		// target is greater than current number, move left boundry
		}else if (target > intarr[mid]){ 
			left = mid + 1; 
		// target is less than current number, move right boundry
		}else{ 
			right = mid -1; 
		} 
	} 
	// target was not found
	if(left > right) printf("The target is not in the array.\n"); 
	recursiveBinarySearch(intarr, 0, ARRSIZE - 1, target);
	return 0;
}

// arr[]: array to sorted
// left: left index
// right: right index starts as (ARR_SIZE - 1)
// t: target (to be found)
int recursiveBinarySearch(int arr[], int left, int right, int t){
	// index of mid 
	int mid; 
	printf("The current range is %d, %d.\n", left, right); 
	if(left<=right){ 
		mid = (left+right)/2; 
		// index found
		if(arr[mid] == t) printf("The index of the target is %d.\n.", mid); 
		// current position number is greater than target --> move right boundry
		else if(arr[mid] > t) recursiveBinarySearch(arr, left, mid-1, t); 
		// current position number is less than target --> move left boundry
		else recursiveBinarySearch(arr, mid+1, right, t);
	} 
	else printf("The target is not found.");
}