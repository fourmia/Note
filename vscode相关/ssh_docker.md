<!--
 * @Author: LZD
 * @Date: 2021-08-11 09:07:28
 * @LastEditTime: 2021-08-11 10:24:47
 * @LastEditors: Please set LastEditors
 * @Description: vscode remote ssh docker 
 * @FilePath: \tools\ssh_docker.md
-->
### 文档说明
此文档用于描述通过vscode连接到远程服务器中正在运行的docker镜像
***

#### Step1: 在Docker中安装SSH
```sh
docker run -it -p 12000:12005 --net=host --privileged=True XXX /bin/bash # 进入容器
yum -y update
yum -y install passwd openssl openssh-server  openssh-clients
```

#### Step2: 创建 **/var/run/sshd/** 目录
```sh
mkdir  /var/run/sshd/
```

#### Step3: 创建公私密钥,输入命令后直接回车
```sh
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ""
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ""
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ""
```

#### Step4: 编辑 **/etc/ssh/sshd_config** 文件
```sh
vim /etc/ssh/sshd_config
```
在文件中找到第17行, 普通模式下输入`:17`定位到17行可看到`#Port 22`，取消注释，建议自行更换至不常用端口 此端口需与进行端口映射的docker端口一致 如 第一步中设定`-p 12000:12000`，意味着将docker的12005端口映射到宿主机器的12000端口，则需要将 **/etc/ssh/sshd_config**中的端口设定改为`Port 12000`,允许root连接,大致在37-39行左右
```
LoginGraceTime 120
PermitRootLogin yes
StrictModes yes
```

#### Step5: 启动ssh服务，并查看是否ssh服务是否正常启动
```sh
/usr/sbin/sshd -D &  # 后台运行ssh服务
ps -ef | grep sshd   # 查询ssh服务是否正常运行
```
如若执行ps命令后，未显示ssh进程，可能为端口占用问题导致，需要返回第四步更换端口重新运行上述命令

#### Step6:设定容器密码
```sh
passwd
```
执行此次命令后需要提交容器

#### Step7:vscode连接远程docker
1. 开启docker镜像（需指定端口映射）
2. 开启`SSH`服务，见 Step5
3. 在vscode扩展中搜索并下载`Remote-SSH`,下载完成左侧边栏显示远程资源管理器图标
4. 点击远程资源管理器，顶部有`SSH TARGETS`便签，便签右侧点击会出现`Configure`选项，选择第一项`C:\Users\Admin\.ssh\config`
```
Host docker
  HostName 172.10.11.160
  User root
  Port 12000
```
其中Host 后面为标签名称，可随意选取，HostName为运行docker的宿主机器，Port为指定的宿主机端口，即`docker -p 12000:12000`参数第一个端口号，注：为保证安全性，不建议在生产服务器使用该方式，仅为便于本地远程服务器调试，建议做好数据备份，防止意外发生

