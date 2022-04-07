#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pre_gen_project.py
@Time    :   2021-10-11 16:51:08
@Author  :   Zheng Zhizhan
@Version :   1.0
@Contact :   740870608@qq.com
@Desc    :   生成项目文件前的hook
'''

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print("""ERROR: The project slug (%s) is not a valid Python module name.
    Please do not use a - and use _ instead""" % module_name)

    # Exit to cancel project
    sys.exit(1)
