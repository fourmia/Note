> 问题

![两数相加](https://raw.githubusercontent.com/fourmia/Picture/main/%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0.png)

> 解法：对于此问题，可以将对应节点数据相加，此时需要注意保存进位情况。当l2结束l1未结束时，需将l1后续节点加上进位值得到新的和，当l1结束l2未结束时同理，最后当两个链表均结束时，需查看是否存在进位，存在进位需新增节点进行存储，具体实现如下：实现过程效率低下，待后续优化

![两数相加解法](https://raw.githubusercontent.com/fourmia/Picture/main/%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0%E8%A7%A3%E6%B3%95.png)