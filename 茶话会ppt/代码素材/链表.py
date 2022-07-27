'''
Author: your name
Date: 2021-11-12 10:18:10
LastEditTime: 2021-11-12 10:44:28
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \A个人笔记\茶话会ppt\代码素材\链表.py
'''
import sys

class Node(object):
    """定义链表节点"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def main():
    node1 = Node(1)
    node2 = Node('2')
    node3 = Node(3)

    node1.next = node2
    node2.next = node3
    i=1
    while node1:
        print(f"第{i}个节点的数据域为{node1.data},数据域字节数为:{sys.getsizeof(node1.data)}")
        node1 = node1.next
        i+=1

if __name__ == "__main__":
    main()