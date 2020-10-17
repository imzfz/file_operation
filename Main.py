#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

SOURCE_DIR_PATH = ''
SOURCE_NAME_REG = r'.*-(.*)-.*'
FILE_TYPE = ''
TARGET_DIR_PATH = ''
TARGET_NAME_REG = ''
IS_FILE = True


def list_files():
    print('源文件夹路径是 : ' + os.path.abspath(SOURCE_DIR_PATH))
    print('目标文件夹路径是 : ' + os.path.abspath(TARGET_DIR_PATH))
    print('源文件正则表达式是 : ' + SOURCE_NAME_REG)
    print('目标文件正则表达式是 : ' + TARGET_NAME_REG)
    print('文件类型是 : ' + FILE_TYPE)

    print('符合要求的文件有 : \n')
    res_files = list()
    for file_name in os.listdir(SOURCE_DIR_PATH):
        file = os.path.join(SOURCE_DIR_PATH, file_name)
        if IS_FILE:
            if os.path.isfile(file) and reg_match(file_name):
                res_files.append(file_name.split('.')[0])
                # res_files.append(file_name)

    for file_name in res_files:
        print(reg_extract(file_name))
        print(file_name)


def reg_match(name):
    if not SOURCE_NAME_REG.strip() == '':
        if re.match(SOURCE_NAME_REG, name):
            return True
        return False
    return True


def reg_extract(name):
    if not SOURCE_NAME_REG.strip() == '':
        m = re.match(SOURCE_NAME_REG, name)
        if m:
            return m.group(1)
    return name


if __name__ == '__main__':
    list_files()
