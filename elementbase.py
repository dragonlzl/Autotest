#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

包含用到的find_element_by_XXX方法的封装、unittest下的断言封装、判断控件是否存在的方法

'''

import unittest
from common import *

class assertElement(unittest.TestCase):

    def assertPage(self,driver, by, value):
        pass_1 = 1
        try:
            find(driver, by, value)
        except:
            #getScreenShot(driver)
            pass_1 = 0
        #try:
        self.assertTrue(pass_1,"页面不正确")

    def assertText(self,driver, by, value, lastelement):  # lastelement通过get_element_text()获取
        #try:
        t1 = get_element_text(driver, by, value)
        pass_1 = 1
        try:
            self.assertNotEqual(t1,"")
        except AssertionError as e:
            #getScreenShot(driver)
            pass_1 = 0
        self.assertTrue(pass_1, "控件text为空")
        pass_2 = 1
        try:
            self.assertEqual(t1.strip(), lastelement.strip())
        except AssertionError as e:
            getScreenShot(driver)
            pass_2 = 0
        self.assertTrue(pass_2, "页面不正确")

    def assertcommon(self,parm):
        self.assertTrue(parm,"执行不通过")


def assertPage(driver,by,value):
    return assertElement().assertPage(driver,by,value)

def assertImage(parm):
    return assertElement().assertcommon(parm)


def find(driver,by,value):

    if by == 'x':
        driver.implicitly_wait(15)
        return driver.find_element_by_xpath(value)
    elif by == 'id': #resource-id
        driver.implicitly_wait(15)
        return driver.find_element_by_id(value)
    elif by == "zb":
        driver.implicitly_wait(15)
        return driver.tap(value)  #坐标直接包含点击事件
    else:
        return '请输入定位方式'



def find_click_text(driver,by,value,by2,assertvalue=""):
    '''
    封装了查找控件，点击控件，每一次操作的断言
    :param driver:
    :param by: 需要进行操作的控件查询方式坐标 如id，zb
    :param value: 控件id或者坐标
    :param by2: 需要进行判断的控件查询方式 如：id，zb
    :param assertvalue: 控件的id或者坐标
    :return:
    '''

    text = get_element_text(driver, by, value)

    if by == 'x':
        print("不存在此方式")

    elif by == 'id': #resource-id

        driver.implicitly_wait(15)
        driver.find_element_by_id(value).click()

        assertElement().assertText(driver,by2,assertvalue,text)

    elif by == "zb":
        print("不存在此方式")

    else:
        return '请输入定位方式'


def find_click_page(driver, by, value, by2, assertvalue=""):
    '''
    封装了查找控件，点击控件，每一次操作的断言
    :param driver:
    :param by: 需要进行操作的控件查询方式坐标 如id，zb
    :param value: 控件id或者坐标
    :param by2: 需要进行判断的控件查询方式 如：id，zb
    :param assertvalue: 控件的id或者坐标
    :param way: 断言方式text or page
    :return:
    '''

    if by == 'x':
        driver.implicitly_wait(15)
        driver.find_element_by_xpath(value).click()
        assertElement().assertPage(driver, by2, assertvalue)

    elif by == 'id':  # resource-id

        driver.implicitly_wait(15)
        driver.find_element_by_id(value).click()
        assertElement().assertPage(driver,by2, assertvalue)

    elif by == "zb":
        driver.implicitly_wait(15)
        driver.tap(value)  # 坐标直接包含点击事件
        assertElement().assertPage(driver, by2, assertvalue)
    else:
        return '请输入定位方式'



def get_element_text(driver,by,value):

    t1 = ""

    if by == "id":
        try:
            t1 = find(driver,by, value).text
        except Exception:
            print("找不到控件:",value)
    return t1

def element_exist(driver,by,value):

    isexist = 1

    try:
        find(driver,by,value)

    except:

        isexist = 0
        print(value,"控件不存在")

    return isexist






