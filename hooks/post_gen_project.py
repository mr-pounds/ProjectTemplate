#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   post_gen_project.py
@Time    :   2021-10-11 16:52:03
@Author  :   Zheng Zhizhan
@Version :   1.0
@Contact :   740870608@qq.com
@Desc    :   项目文件生成后的hook
"""

# here put the import lib
PROJECT_NAME = "{{cookiecutter.project_slug}}"

if __name__ == "__main__":

    # Enter project directory
    print(
        """项目创建成功，请继续执行以下操作完成项目创建：
    cd %s
    git init
    pipenv install --dev --python 3.8
    pipenv run pre-commit install
    """
        % PROJECT_NAME
    )
