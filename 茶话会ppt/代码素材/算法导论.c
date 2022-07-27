#include <stdio.h>

// void main(){
//     int sum = 0, n = 100;      /* 执行一次 */
//     sum = ( 1 + n ) * n / 2;   /* 执行一次 */
//     printf("%d\n", sum);       /* 执行一次 */
// }

void main(){
    int n =5;                /* 执行一次 */
    for(int i=1; i<=n; i++){            /* 执行n次 */
        for(int j=1; j<=n; j++){            /* 执行n次 */
            printf("(%d,%d)\n", i,j);               /* 执行一次 */
        }
    }
}