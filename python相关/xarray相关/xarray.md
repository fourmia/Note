<!--
 * @Author: your name
 * @Date: 2021-08-27 09:14:35
 * @LastEditTime: 2021-09-15 17:50:42
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
### 选取指定经纬度时出现的异常问题
> 在上一步出现选取指定经纬度异常时，若出现 *gives keyerror： not all values found in index*, 一般是由于浮点数精度原因造成的，可采用下面方式处理
```python
lat_ = np.round(lat, 2)
lon_ = np.round(lon, 2)
dr['latitude'] = np.round(dr.latitude.values, 2)
dr['longitude'] = np.round(dr.longitude.values, 2)
dr_selected = dr.sel(latitude=lat,longitude=lon)
```

### 简单Nc文件写入