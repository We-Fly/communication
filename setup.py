# 这个文件是用来快速安装软件包的
# 推荐在程序运行之前运行一次本程序安装所需软件包
# import pip
import argparse
import subprocess
import sys
# use python type hints to make code more readable
from typing import List, Optional


def pip_install(proxy: Optional[str], args: List[str]) -> None:
    if proxy is None:
        # pip.main(["install", f"--proxy={proxy}", *args])
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-i", f"https://pypi.tuna.tsinghua.edu.cn/simple", *args],
            # capture_output=False,
            check=True,
        )
    else:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", f"--proxy={proxy}",*args],
            # capture_output=False,
            check=True,
        )


def install():
    parser = argparse.ArgumentParser(description="install requirements")
    parser.add_argument(
        "--proxy",
        default=None,
        type=str,
        help="specify http proxy, [http://127.0.0.1:1080]",
    )
    args = parser.parse_args()
    # 如果后期有需要添加的包就写这个列表里
    pkgs = f"""
    pyserial
    pyserial_asyncio
    """

    for line in pkgs.split("\n"):
        # handle multiple space in an empty line
        line = line.strip()

        if len(line) > 0:
            # use pip's internal APIs in this way is deprecated. This will fail in a future version of pip.
            # The most reliable approach, and the one that is fully supported, is to run pip in a subprocess.
            # ref: https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
            # pip.main(['install', *line.split()])

            pip_install(args.proxy, line.split())

    print("\nsuccessfully installed requirements!")
def checkPkgs():
    try:
        import serial
        import serial_asyncio
        print("requirements are installed")
    except ImportError:
        print("requirements not Installed")
        install()

if __name__ == "__main__":
    checkPkgs()
