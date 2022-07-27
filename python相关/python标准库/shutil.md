<!--
 * @Author: your name
 * @Date: 2021-09-16 09:45:21
 * @LastEditTime: 2021-09-16 09:54:19
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \A个人笔记\python相关\python标准库\shutil.md
-->
## shutil 模块
> `os` 模块是 Python 标准库中一个重要的模块，里面提供了对目录和文件的一般常用操作。而 Python 另外一个标准库——`shutil` 库，它**作为 `os` 模块的补充**，提供了**复制、移动、删除、压缩、解压**等操作，这些 `os` 模块中一般是没有提供的。但是需要注意的是：`shutil` 模块对压缩包的处理是调用 `ZipFile` 和 `TarFile` 这两个模块来进行的。`src`为源文件，`dst`为目标文件。


![shutil常用操作](shutil思维导图.png "shutil常用操作")
