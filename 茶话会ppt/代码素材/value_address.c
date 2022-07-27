#include <stdio.h>

void swap_value(int a, int b){
    // 进行a和b值交换
    a = a ^ b;
    b = a ^ b;
    a = b ^ a;
    // printf("value: a is %d, b is %d\n", a, b);
} 

void swap_address(int* a, int* b){
    // 进行a和b值交换
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *b ^ *a;
    // printf("address: a is %d, b is %d\n", *a, *b);
} 

void main(){
    int a = 10;
    int b = 5;
    // 值传递
    printf("begin swap --> a is %d, b is %d\n", a, b);
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    swap_value(a, b);
    printf("value swap --> a is %d, b is %d\n", a, b);
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    // 地址传递
    swap_address(&a, &b);
    printf("address swap --> a is %d. b is %d\n", a, b);
}