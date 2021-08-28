<!--
 * @Author: your name
 * @Date: 2021-08-27 09:14:35
 * @LastEditTime: 2021-08-27 15:46:08
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Editi
 * @FilePath: \A个人笔记\xarray相关\xarray.md
-->
## 写在前面
> 此文档主要用于记录在xarray使用过程中遇到的一些问题，供以后使用查阅
***
### 选取指定经纬度范围内数据
```python
dr = xr.open_dataset(r'XXX')
lat = np.arange(begin_lat,end_lat,step)
lon = np.arange(begin_lon,end_lon,step)
dr_selected = dr.sel(latitude=lat,longitude=lon)
```