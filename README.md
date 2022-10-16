# 无人机控制库

此仓库可以通过python代码对无人机进行操控。

## Usage

你需要安装以下库

```bash
pip install pyserial_asyncio
pip install pyserial
```

cd到项目文件夹，在终端输入`pip install -r packages -i https://pypi.tuna.tsinghua.edu.cn/simple `并回车运行，使用tuna镜像源下载所需软件包

如果你有代理服务器可以加上代理服务器地址，例如`pip install -r packages --proxy http://127.0.0.1:7890`

## TODO

- [x] 实现串口通信
- [ ] 实现NCLink协议
- [ ] 实现飞机解锁，起飞和降落
- [ ] 实现基础的飞机操控
- [ ] 实现无人机的定高操作
- [ ] 实现接收飞机数据
