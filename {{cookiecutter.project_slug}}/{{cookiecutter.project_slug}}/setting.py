import os
import yaml

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf_path = os.path.join(project_path, 'conf.yaml')

# 读取项目设置
with open(conf_path, 'r', encoding='utf-8') as f:
    conf = yaml.load(f.read())
