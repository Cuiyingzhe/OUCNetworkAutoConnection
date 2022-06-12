# OUCNetworkAutoConnection
An automatically reconnection tool for OUC campus network.

使用方法：

下载 https://github.com/Cuiyingzhe/OUCNetworkAutoConnection/releases/download/v2.0/yxrz.exe 并运行，输入校园网账号和密码即可

打包方法：

`pyinstaller -F -p 'your python package directory' yxrz.py`

更多信息见https://blog.csdn.net/cyzzym000/article/details/124145635

注意，仅支持通过`yxrz.ouc.edu.cn`登录认证的办公室有线网用户。

*可将yxrz.py中输入的用户名密码直接赋值，打包为yxrz.exe后放入windows开机启动项中以实现自动启动。实测(Win11)在输入windows用户名密码前，该程序即可启动，如向日葵等远程软件也设置为开机自动启动，则可以实现远程主机意外重启后的远程连接。
