#include<stdio.h>
#include<stdlib.h>
#include<time.h>

typedef struct Node{
    float data;
    struct Node *next;
} Node;

typedef struct Node *LinkList;

LinkList CreateListTail(LinkList L, int n){
    LinkList p, r;
    int i;
    srand(time(0));
    L = (LinkList)malloc(sizeof(Node));
    r = L;
    for (i=0; i<n; i++){
        p = (LinkList)malloc(sizeof(Node));
        p->data = rand()%100+1;
        r->next=p;
        r = p;
    }
    r->next = NULL;
    return L;
}

void display(LinkList p){
    LinkList temp=p;//将temp指针重新指向头结点
    //只要temp指针指向的结点的next不是Null，就执行输出语句。
    printf("头节点地址为: %p\n", p);
    printf("头节点next地址为: %p\n", p->next);
    int i =0;
    while (temp->next) {
        temp=temp->next;
        printf("第%d个节点地址为: %p \t", i+1, temp);
        printf("%.2f\t",temp->data);
        printf("第%d个节点data域地址为: %p \t", i+1, &(temp->data));
        printf("第%d个节点next域地址为: %p \n", i+1, temp->next);
        i+=1;
    }
    printf("\n");
}

void main(){
    int n =10;
    LinkList L = NULL;
    printf("Node节点字节数:%ld\n",sizeof(Node));
    LinkList first_pointer = CreateListTail(L, n);
    display(first_pointer);

}