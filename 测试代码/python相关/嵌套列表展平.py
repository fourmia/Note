'''
Author: your name
Date: 2021-09-28 11:21:41
LastEditTime: 2021-09-28 11:24:18
LastEditors: your name
Description: In User Settings Edit
FilePath: \A个人笔记\测试代码\python相关\嵌套列表展平.py
'''
import unittest
from logzero import logger
from collections import Iterable

def flattening_series(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            logger.debug(f"x_Iterable is:{x}")
            yield from flattening_series(x)    # flattening_series即是委托生成器，也是子生成器， 通过debug进行验证
        else:
            logger.debug(f"only element x is:{x}")
            yield x

class TestflatteningSeries(unittest.TestCase):
    def test_nested_series(self):
        self.assertEqual(list(flattening_series(['dog', ['pig', ['mouse','horse']], 'cat'])),
                                                ['dog', 'pig', 'mouse', 'horse', 'cat'])

if __name__ == '__main__':
    unittest.main()