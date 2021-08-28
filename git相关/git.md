<!--
 * @Author: your name
 * @Date: 2021-08-27 15:47:49
 * @LastEditTime: 2021-08-28 17:11:19
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \A个人笔记\git相关\git.md
-->
## Git操作笔记
***
### 第一步:安装及配置

> 此步主要进行`git`安装及配置，运行以下命令安装,根据自己邮箱生成`ssh`,接着查看`ssh`文件夹下的`id_res_pub`，进入`github/gitlab`,在**SSH KEY**栏粘贴生成的**KEY**，完成后验证是否设置成功,验证成功后配置用户名及密码，配置完成后可以添加要上传的远程地址，就可以愉快的玩耍了
```sh
yum install -y git    # centos install
ssh-keygen -t rsa -C "your_email@xx.com"
cat ~/.ssh/id_rsa.pub

ssh -T git@github.com     # 看到successfully表示连接上github

git config --global user.name "your name"
git config --global user.email "your_email@youremail.com"

git init    # 先初始化，不然会报错呦
git remote add origin git@github.com:yourName/yourRepo.git   # 连接远程库
```

### 第二步：向远程推送代码
> 通过第一步，我们完成了远程库的连接操作，接下来，让我们开始探索代码推送
```sh
git branch  # 查看当前分支
    > *master  # *为当前所在分支
       main

git add XXX  # 添加待推送文件
git status   # 查看分支状态
git commit -m "My first Test" # 提交
git push origin master:master # 由于github远程仅存main分支，因此提交时把本地的master分支也提交到远程
git branch -a # 查看所有分支

```
