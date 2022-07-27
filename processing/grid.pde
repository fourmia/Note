'''
Author: your name
Date: 2021-11-05 11:01:02
LastEditTime: 2021-11-05 11:41:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \A个人笔记\processing\grid.py
'''
# 为图像绘制青色网格

# 设置x的最大值及最小值
xmin = -10
xmax = 10

# y的最小值及最大值
ymin = -10
ymax = 10

# 计算x值及y值范围
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 600)
    xscl = width / rangex
    yscl = -height / rangey

def draw():
    global xscl, yscl
    background(255)    # set background with white
    translate(width/2, height/2)    # 将原点从左上角平移至屏幕中心
    grid(xscl, yscl)
    graphFunction()


def grid(xscl, yscl):
    # 青色的线
    strokeWeight(1)    # 设置线宽
    stroke(0,255,255)  # 设置先颜色为青色（最弱的红色、最强的绿色、最强的蓝色）

    # 在processing中需要四个参数来绘制一条线，分别是线段起点和中点的x、y坐标
    for i in range(xmin, xmax+1):
        # line(i, ymin, i,ymax)  # 绘制小正方形，原因是屏幕像素坐标范围在(-300, 300)但是线的坐标范围在(-10， 10)，因此需要将比例尺相乘
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)  # 绘制竖直线
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)  # 绘制水平线

    stroke(0,0,0)    # 设置黑色的轴
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)

def f(x):
    return x**2

def graphFunction():
    x = xmin
    stroke(255,0,0)
    while x <= xmax:
        fill(0)
        line(x*xscl, f(x)*yscl, (x+0.1)*xscl, f(x+0.1)*yscl)
        x+=0.1