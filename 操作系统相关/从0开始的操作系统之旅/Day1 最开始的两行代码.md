<!--
 * @Author: LiZedong 15516926476@163.com
 * @Date: 2022-09-28 17:30:26
 * @LastEditors: LiZedong 15516926476@163.com
 * @LastEditTime: 2022-10-10 18:06:27
 * @FilePath: \A个人笔记\操作系统相关\从0开始的操作系统之旅\Day1 最开始的两行代码.md
 * @Description: 
 * 
 * Copyright (c) 2022 by LiZedong 15516926476@163.com, All Rights Reserved. 
-->
### 开机
1.
    + 问题: 请根据下图，描述电脑开机过程发生的事情
    ![](https://mmbiz.qpic.cn/mmbiz_png/GLeh42uInXSsqVrEibE9LXat88ha3emc5Jicib9Ou8Gn4aDBdv0LQZ4flibcPkZVtYiaCHE4zBgcbBqufFY4C6zJgoQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
    + 回答:
    
        <font color='#38cc60'> 如图，在按下电源键后，硬件电路将`CPU`的`cs:ip`寄存器强制置为某一个值``，即BIOS所在地址，运行BIOS中程序,其会读取硬盘的第一扇区，将读取到的512字节加载进内存`0x7c00`至`0x7dff`的位置，然后`CPU`会根据跳转指令将`cs:ip`置于`0x7c00`位置，运行其中代码。</font>

    + 思考过程的疑惑：

        <font color='#00F5FF'>
        此处BIOS所在地址存疑，不清楚：BIOS所在位置为只读存储器中，其应该是映射到主存的某一地址处，该地址即为BIOS地址，将`cs：ip`置于该地址运行即可。

        BIOS是否会加载进内存：现代计算机均按照冯.诺依曼体系架构，所有程序均在主存储器中运行

        确定是硬盘第一扇区吗：此处表述有误，此处主要是想运行MBR主引导记录，应当为MBR程序所在扇区，MBR判定是根据扇区的最后两个字节判定，若为`0x55,0xaa`,则认为其为启动区
        </font>