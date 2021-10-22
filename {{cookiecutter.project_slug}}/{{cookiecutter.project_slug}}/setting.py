import os

import yaml

# 项目根目录
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库文件地址
DB_DIR = os.path.join(project_path, "db")

# 日志文件地址
LOG_DIR = os.path.join(project_path, "log")

# 静态或模板文档地址
TEMPLATE = os.path.join(project_path, "template")

# 项目配置文件地址
conf_path = os.path.join(project_path, "conf.yaml")

# 读取项目设置
with open(conf_path, "r", encoding="utf-8") as f:
    conf = yaml.load(f.read(), Loader=yaml.FullLoader)
