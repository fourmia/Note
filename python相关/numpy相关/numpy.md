<!--
 * @Author: your name
 * @Date: 2021-08-31 16:54:32
 * @LastEditTime: 2021-08-31 17:09:24
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \A个人笔记\python相关\numpy相关\numpy.md
-->
## 写在前面
此文档主要用于对numpy数据处理遇到的问题进行记录

### numpy 对指定索引一定范围的数据进行填充
```python
import numpy as np
lat,lon = np.linspace(xxx,xxx,xxx), np.linspace(xxx,xxx,xxx)
data = np.zeros(shape=(len(lat), len(lon)))

change_lat, change_lon = [xxx,xxx,...],[xxx,xxx,...]
for lat_ele, lon_ele in zip(change_lat, change_lon):
    lat_index, lon_index = np.where(lat==lat_ele)[0][0],np.where(lon==lon_ele)[0][0]
    data[max(0, x-20):x+20, max(0,y-20):y+20]=1 #取该格点周围20km的格点置为1


```