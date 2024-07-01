import os

from dotenv import load_dotenv

# 设置工作路径，以免导致相对路径引用错误的问题
os.chdir(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))

# 读取环境变量文件，非.env则需手动指定
load_dotenv()
# 获取环境变量
# VARIABLE= os.getenv("VARIABLE")
