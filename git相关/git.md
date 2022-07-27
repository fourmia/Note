<!--
 * @Author: your name
 * @Date: 2021-08-27 15:47:49
 * @LastEditTime: 2022-01-23 11:19:04
 * @LastEditors: LiZedong <15516926476@163.com>
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

### 本地分支合并
> 开发过程中个人分支采用`feature`分支，整体开发使用`develop`分支，完成功能开发后需要进行分支合并，将本地分支`feature`合并至本地分支`develop`，而在合并分支中若两个分支存在冲突则需要解决冲突后进行合并，某些情况下，对于不同文件的更改，我们更期望屏蔽掉更改的文件(由于更改尚未完成)，进行冲突合并，这个时候可以采用`git stash`命令进行。
```sh
git stash  # 将所有未提交的更改进行保存，用于后续恢复当前目录（包括暂存及非暂存的）
git stash save "input your tips" # 通过添加save可以给stash添加新的message,进行版本记录

git stash pop  # 用于将缓存堆栈中的第一个stash删除，并将对应修改应用到当前的工作目录下

git stash apply    # 用于将缓存堆栈中的stash多次应用到工作目录中，但并不删除stash拷贝。

git stash list    #  用于查看现有的list

git stash drop    #  后面可以跟着stash名字进行移除stash,git stash clear命令，删除所有缓存的stash。

git stash show   # 后面可以跟着stash名字,查看指定stash的diff,在该命令后面添加-p或--patch可以查看特定stash的全部diff

git stash branch testchanges   # 从stash创建分支,检出你储藏工作时的所处的提交，重新应用你的工作，如果成功，将会丢弃储藏。
```


### 删除分支
> 在开发过程中，本地开发一般采用feature分支，若操作不慎，将feature分支推送至远端，可采用以下命令进行删除.
```sh
git push origin --delete dev_s  # dev_s为要删除的远端分支
git branch -d dev    # dev为要删除的本地分支
```

### 更新分支
```bash
git branch -a    # 查看所有分支
git remote update origin --prune    # 更新远程分支列表
```