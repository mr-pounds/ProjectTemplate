#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   post_gen_project.py
@Time    :   2021-10-11 16:52:03
@Author  :   Zheng Zhizhan
@Version :   1.0
@Contact :   740870608@qq.com
@Desc    :   项目文件生成后的hook
'''

# here put the import lib
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = "{{cookiecutter.project_slug}}"

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    # Enter project directory
    print("""项目创建成功，请继续执行以下操作完成项目创建：
    cd %s
    git init
    pipenv install --dev --python 3.8
    """% PROJECT_NAME)

