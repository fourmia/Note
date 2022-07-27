#include<stdio.h>

void main(){
    int my_array[10] = 0;

    for(int i=1; i<=10; i++){
        my_array[i-1] = i;
    }
}