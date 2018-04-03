#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

case、报告、截图要用到的文件操作方法、时间获取方法、路径方法

'''

import time,os

def getpath():
# 当前文件路径
    case_path = os.path.join(os.getcwd())
    return case_path


def getScreenShot(driver,test_method_name = ""):

    now = getTime()
    path = new_dir()
    driver.get_screenshot_as_file(path + "\\" + test_method_name + now + ".png")

def getTime():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    return now

def reportpath():

    now = getTime()
    path = os.path.join(os.getcwd(), 'report') + "\\report" + now
    os.makedirs(path)

    return path

def new_dir(path = r"D:\python36\autotest\report"):
    lists = os.listdir(path)                                    #列出目录的下所有文件和文件夹保存到lists
    print(os.path.getmtime(path))
    lists.sort(key=lambda fn:os.path.getmtime(path + "\\" + fn))#按时间排序
    dir_new = os.path.join(path,lists[-1])                     #获取最新的文件保存到file_new
    return dir_new