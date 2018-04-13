#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

case、报告、截图要用到的文件操作方法、时间获取方法、路径方法

'''

import time,os,sys

def getpath():         #获取用例的执行路径
# 当前文件路径
    case_path = os.path.join(sys.path[0])
    return case_path


def getScreenShot(driver,test_method_name = ""):       #截图方法，图片利用方法名+时间来命名，截图地址会放在最新的报告文件夹中，因为每次运行用例，都会先创建文件夹再有截图

    now = getTime()
    path = new_dir()
    driver.get_screenshot_as_file(path + "\\" + test_method_name + "_" + now + ".png")

def getTime():   #获取时间，命名要用该时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    return now

def reportpath():        #每次运行，都会创建一个最新的文件夹，并返回地址，用于存放报告

    now = getTime()
    path = os.path.join(sys.path[0], 'report') + "\\report" + now
    os.makedirs(path)

    return path

def new_dir(path = r"D:\python36\autotest\report"):             #获取指定路径下，最新的文件夹，返回最新的文件夹

    lists = os.listdir(path)                                    #列出目录的下所有文件和文件夹保存到lists
    #print(os.path.getmtime(path))
    lists.sort(key=lambda fn:os.path.getmtime(path + "\\" + fn))#按时间排序
    dir_new = os.path.join(path,lists[-1])                     #获取最新的文件保存到file_new
    return dir_new

def get_find_zb(driver):

    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]

    width_zb = (470 * width) / 540
    height_zb = (935 * height) / 960

    return [(width_zb, height_zb)]

def get_return_zb(driver):

    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]

    width_zb = (42 * width) / 540
    height_zb = (75 * height) / 960

    return [(width_zb, height_zb)]