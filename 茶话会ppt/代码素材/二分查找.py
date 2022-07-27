'''
Author: your name
Date: 2021-11-24 17:42:08
LastEditTime: 2021-11-25 09:13:42
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \A个人笔记\茶话会ppt\代码素材\二分查找.py
'''
import array
import logging
# from logzero import logger
from bisect import bisect_left

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s   %(levelname)s   %(message)s')

def index(sorted_series, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(sorted_series, x)
    if i != len(sorted_series) and sorted_series[i] == x:
        return i
    raise ValueError

def loop_search(sorted_series, x):
    for idx,i in enumerate(sorted_series):
        if i != len(sorted_series) and sorted_series[i] == x:
            return idx
        raise ValueError

def main():
    find_value = 80
    series = array.array('i', range(0,100,2))
    binary_result = index(series, find_value)
    print(f"binary_index is:{binary_result}")
    # logging.info(f"binary_index is:{binary_result}")
    loop_result = index(series, find_value)
    print(f"loop_index is:{loop_result}")
    # logging.info(f"loop_index is:{loop_result}")

if __name__ == '__main__':
    main()
