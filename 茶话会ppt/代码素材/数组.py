'''
Author: your name
Date: 2021-11-11 14:35:05
LastEditTime: 2021-11-11 18:04:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \A个人笔记\茶话会ppt\代码素材\数组.py
'''
import array

def main():
    test_array = array.array('i', [1000,2,3,4])
    t = test_array
    print("修改前test_array 地址为:", id(test_array))
    print("修改前t 地址为:", id(t))
    print("修改前test_array[1]地址为:", id(test_array[1]))
    print("修改前t[1]地址为:",id(t[1]))
    d = memoryview(test_array)
    d[1] = 1001
    print("修改后test_array 地址为:", id(test_array))
    print("修改后t 地址为:", id(t))
    print("修改后test_array[1] 地址为:", id(test_array[1]))
    print("修改后t[1] 地址为:", id(t[1]))
    print(test_array)
    print(t)

# def main():
#     test_array = array.array('i', [1000,2,3,4])
#     for i in range(len(test_array)):
#         print(f"修改前test_array[{i}]地址为: {id(test_array[i])}")
#     print(f"test_array is: {test_array}")

#     for i,j in enumerate(range(500,504)):
#         test_array[i] = j
#         print(f"修改后test_array[{i}]地址为: {id(test_array[i])}")
#     print(f"test_array is: {test_array}")

if __name__ == "__main__":
    main()