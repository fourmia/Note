'''
Author: your name
Date: 2021-11-24 10:19:05
LastEditTime: 2021-11-25 09:43:30
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \A个人笔记\茶话会ppt\代码素材\算法分析.py
'''
import array

def binary_search(series, item):
    low = 0
    high = len(series) - 1
    low_series = array.array('i',[])
    high_series = array.array('i',[])
    guess_series = array.array('i',[])
    while low <= high:
        mid = low + ((high - low) >> 1)
        guess = series[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        low_series.append(series[low])
        high_series.append(series[high])
        guess_series.append(guess)
    return None

if __name__ == '__main__':
    my_array = array.array('i', range(1,100))
    print(f"99 in my_array index is:{binary_search(my_array,99)}")