"""
Name         : 
Description  : 
Version      : 1.0.1
Author       : zzz
Date         : 2024-07-01 09:36:28
LastEditors  : zzz
LastEditTime : 2024-07-01 11:16:15
"""

import os

from dotenv import load_dotenv

# 设置工作路径，以免导致相对路径引用错误的问题
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 读取环境变量文件，非.env则需手动指定
load_dotenv()
# 获取环境变量
# VARIABLE= os.getenv("VARIABLE")
