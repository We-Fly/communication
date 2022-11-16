# 无人机控制库 UAV control library

此仓库可以通过python代码对无人机进行操控。

## 使用方法 Instructions

你需要通过终端安装以下库

You need to install the following python libraries via command line

```bash
pip install pyserial_asyncio
pip install pyserial
```

### 自动初始化 Auto setup

#### 方法1 method 1

cd到项目文件夹，在终端输入`pip install -r packages -i https://pypi.tuna.tsinghua.edu.cn/simple `并回车运行，使用tuna镜像源下载所需软件包

如果你有代理服务器可以加上代理服务器地址，例如`pip install -r packages --proxy http://127.0.0.1:7890`

#### 方法2 method 2

cd到项目文件夹，在终端输入`python setup.py `并回车运行，使用tuna镜像源下载所需软件包

如果你有代理服务器可以加上代理服务器地址，例如`python setup.py --proxy http://127.0.0.1:7890`

## TODO

- [x] 实现串口通信
- [ ] 实现NCLink协议
- [ ] 实现飞机解锁，起飞和降落
- [ ] 实现基础的飞机操控
- [ ] 实现无人机的定高操作
- [ ] 实现接收飞机数据
