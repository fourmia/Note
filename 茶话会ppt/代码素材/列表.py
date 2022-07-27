'''
Author: your name
Date: 2021-11-11 18:08:02
LastEditTime: 2021-11-11 18:14:09
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \A个人笔记\茶话会ppt\代码素材\列表.py
'''
import copy

def main():
    list1 = [1, 2, 3, [1,2,3]]
    list1_copy = copy.copy(list1)
    list1_decopy = copy.deepcopy(list1)

    list1[-1][0] = 100
    print(list1)

    f = [['_']]*3
    f[0][0] =1
    print(f)
    f[0][0]= 2
    print(f)

if __name__ == '__main__':
    main()