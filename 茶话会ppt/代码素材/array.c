#include <stdio.h>

void main(){
    int array_test[10];
    for(int i=0;i<=5;i++)
    {
        array_test[i] = i;
        printf("第%d个元素的值为:%d,字节数:%ld,地址为: %p \n", i, array_test[i], sizeof(array_test[i]), &(array_test[i]));
    }
    array_test[5] = 100;
    printf("第%d个元素的值为:%d, 地址为: %p \n", 5, array_test[5], &(array_test[5]));

}
