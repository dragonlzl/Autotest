#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
包含测试用例，错误截图的代码
1.测试前先退出登录
2.微信和QQ都不需要登录，暂时还没有写微信和QQ登录后的相关用例
3.创作页面，H5相关的，还是需要人工测试
'''
from appium import webdriver
from elementbase import *
import unittest
import HTMLTestRunner
from elementdata import *
from common import *

# 用例路径
#case_path = os.path.join(os.getcwd())
# 报告存放路径
#report_path = os.path.join(os.getcwd(), 'report')


def getImage(function):
    #@wraps(function)
    def get_ErrImage(self, *args, **kwargs):
        pass_3 = 1
        try:
            function(self, *args, **kwargs)
        except Exception as e:
            pass_3 = 0
            getScreenShot(self.driver)
            print(e)

        assertImage(pass_3)

    return get_ErrImage

class testCodemao(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '80a8d0db'
        desired_caps['appPackage'] = 'xxxxxx'  # APK包名
        desired_caps['appActivity'] = "xxxxxxx"#'com.qihoo.util.StartActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.close_app()

    @getImage #使用装饰器
    def test000_login(self):

        self.driver.wait_activity('com.codemao.box.module.welcome.MainActivity', 10)
        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id", page_wode_element["头像按钮"])
        find_click_page(self.driver, "id", page_wode_element["头像按钮"], "id", page_login_element["登录按钮"])
        find_click_text(self.driver, "id", page_login_element["登录按钮"], "id", page_login_element["确认登录按钮"])
        find(self.driver, "id",page_login_element["帐号输入框"]).send_keys(account["测试服帐号1"])
        find(self.driver, "id",page_login_element["密码输入框"]).send_keys(account["测试服密码1"])
        find_click_page(self.driver, "id", page_login_element["确认登录按钮"], "id", page_wode_element["退出登录按钮"])

        print("登录测试完毕")

    @getImage
    def test001_page_one(self):

        find_click_page(self.driver, "id",page_one_element["游戏按钮"],"id",page_one_element["首页标题栏"]) #点击游戏

        find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
        find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"],"id", page_one_element["首页标题栏"]) #返回
        print("推荐页测试完毕")

        find_click_page(self.driver, "id", page_one_element["热门页签"],"id", page_zuopin_element["作品列表-作品框"])  #热门
        find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
        find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"],"id", page_one_element["首页标题栏"])
        print("热门页测试完毕")

        find_click_page(self.driver, "id", page_one_element["最新页签"],"id", page_zuopin_element["作品列表-作品框"]) # 最新
        find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
        find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"],"id", page_one_element["首页标题栏"])
        print("最新页测试完毕")

        find_click_page(self.driver, "id", page_one_element["视频按钮"], "id", page_one_element["视频框"]) #视频页面
        find_click_page(self.driver, "id", page_one_element["视频-公开课按钮"], "id", page_one_element["视频框"])
        print("视频页测试完毕")

        print("首页主页测试完毕")

    @getImage
    def test002_find(self):

        find_click_page(self.driver, "id", page_one_element["搜索按钮"], "id", page_search_element["搜索内容"])  # 搜索
        find(self.driver, "id", page_search_element["搜索内容"]).send_keys("123")
        #driver.press_keycode(84)
        #self.assertIn("123", get_element_text(driver, "id", "com.codemao.box:id/name_tv").strip())
        find_click_page(self.driver, "zb", [(495,920)], "id",page_search_element["搜索内容"])
        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品名"]):
            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id", page_zuopin_element["作品详情-作品名"])
            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], page_search_element["搜索内容"])
            find_click_page(self.driver, "id", page_search_element["搜索返回"], "id", page_one_element["首页标题栏"])  # 搜索返回
        else:
            assertPage(self.driver,"id",page_search_element["没有内容图片"])
            print(" 列表为空")
        print("搜索页测试完毕")

    @getImage
    def test003_shoucang_dianzan(self):   #收藏和点赞

        find_click_page(self.driver, "id", page_one_element["游戏按钮"], "id", page_one_element["首页标题栏"])  # 推荐
        find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id", page_zuopin_element["作品详情-作品名"])

        t1 = get_element_text(self.driver, "id", page_zuopin_element["作品详情-收藏/取消收藏"])

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-收藏/取消收藏"], "id", page_zuopin_element["作品详情-作品名"])

        self.assertNotEqual(t1.strip(), get_element_text(self.driver, "id",page_zuopin_element["作品详情-收藏/取消收藏"]).strip(),"收藏状态没有改变")

        t1 = get_element_text(self.driver, "id", page_zuopin_element["作品详情-点赞/取消点赞"])

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-点赞/取消点赞"], "id", page_zuopin_element["作品详情-作品名"])

        self.assertNotEqual(t1.strip(), get_element_text(self.driver, "id", page_zuopin_element["作品详情-点赞/取消点赞"]).strip(),"点赞状态没有改变")

        print("收藏点赞测试完毕")

    @getImage
    def test004_fenxiang(self):

        find_click_page(self.driver, "id", page_one_element["热门页签"], "id", page_zuopin_element["作品列表-作品框"])
        find_click_page(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-分享"], "id", page_zuopin_element["作品详情-分享到"])

        find(self.driver, "x", "//android.widget.TextView[contains(@text,'微信好友')]").click()  # 分享方式其中一个
        assertPage(self.driver,"id",page_fenxiang_element["微信标题栏"])
        #find_click_page(self.driver,"id",page_fenxiang_element["微信登录框"])
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        print("未登录时微信好友跳转完成")

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-分享"], "id", page_zuopin_element["作品详情-分享到"])
        find(self.driver, "x", "//android.widget.TextView[contains(@text,'朋友圈')]").click()  # 分享方式其中一个
        assertPage(self.driver, "id", page_fenxiang_element["微信标题栏"])
        #find_click_page(self.driver, "id", page_fenxiang_element["微信登录框"])
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        print("未登录时微信朋友圈跳转完成")

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-分享"], "id", page_zuopin_element["作品详情-分享到"])
        find(self.driver, "x", "//android.widget.TextView[contains(@text,'QQ')]").click()  # 分享方式其中一个
        assertPage(self.driver, "id", page_fenxiang_element["QQ登录标题栏"])
        #find_click_page(self.driver, "id", page_fenxiang_element["QQ登录标题栏"])
        self.driver.press_keycode(4)
        print("未登录时QQ跳转完成")

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-分享"], "id", page_zuopin_element["作品详情-分享到"])
        find(self.driver, "x", "//android.widget.TextView[contains(@text,'QQ空间')]").click()  # 分享方式其中一个
        assertPage(self.driver, "id", page_fenxiang_element["QQ登录标题栏"])
        #find_click_page(self.driver, "id", page_fenxiang_element["QQ登录标题栏"])
        self.driver.press_keycode(4)
        print("未登录时QQ空间跳转完成")

        self.driver.press_keycode(4)
        print("分享测试完成")

    @getImage
    def test005_page_wode(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id", page_wode_element["个人信息编辑按钮"])  # 我的

        find_click_text(self.driver, "id", page_wode_element["设置按钮"], "id",page_wode_set_element["设置标题栏"]) #设置

        find_click_page(self.driver, "id", page_wode_set_element["清除缓存按钮"], "id", page_wode_set_element["提示弹窗标题栏"])  # 清除缓存
        find_click_page(self.driver, "id", page_wode_set_element["取消按钮"], "id", page_wode_set_element["清除缓存按钮"])  # 取消

        find_click_page(self.driver, "id", page_wode_set_element["清除缓存按钮"], "id", page_wode_set_element["提示弹窗标题栏"])
        find_click_page(self.driver, "id", page_wode_set_element["确定按钮"], "id", page_wode_set_element["清除缓存按钮"])  # 确定

        find_click_page(self.driver, "zb", [(42, 75)], "id", page_wode_element["我的收藏按钮"])#返回
        print("我的-设置测试完毕")

        find_click_page(self.driver, "id", page_wode_element["关于编程猫按钮"], "id", page_wode_guanyu_element["关于标题栏"]) #关于
        find_click_page(self.driver, "zb", [(42, 75)], "id", page_wode_element["我的收藏按钮"])  # 返回
        print("我的-关于测试完毕")

    @getImage
    def test006_userdetial_change(self): #改个人信息

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id", page_wode_element["个人信息编辑按钮"])  # 我的

        find_click_page(self.driver, "id", page_wode_element["个人信息编辑按钮"], "id", page_wode_xiugai_element["个人资料标题栏"])

        find_click_text(self.driver, "id", page_wode_xiugai_element["昵称栏"], "id",page_wode_xiugai_element["内容编辑框"])

        find(self.driver, "id", page_wode_xiugai_element["内容编辑框"]).set_text("TeStNO1")  # sehzh名字

        find_click_page(self.driver, "id", page_wode_xiugai_element["确定编辑按钮"], "id", page_wode_xiugai_element["昵称栏"]) #确定改名

        print("改名完毕")

        find_click_page(self.driver, "id", page_wode_xiugai_element["头像栏"], "id", page_wode_xiugai_element["图片"]) #点击头像

        find_click_page(self.driver, "id", page_wode_xiugai_element["图片选择"], "id", page_wode_xiugai_element["图片"]) #选头像

        find_click_page(self.driver, "id", page_wode_xiugai_element["选择完成按钮"], "id", page_wode_xiugai_element["头像栏"]) #完成

        print("改头像完毕")

        find_click_page(self.driver, "id", page_wode_xiugai_element["性别栏"], "id", page_wode_xiugai_element["编辑框标题栏"]) #点击性别

        find_click_page(self.driver, "id", page_wode_xiugai_element["女性选择"], "id", page_wode_xiugai_element["编辑框标题栏"]) #选择性别 女

        t1 = get_element_text(self.driver, "id", page_wode_xiugai_element["女性选择"]) #女

        find_click_page(self.driver, "id", page_wode_xiugai_element["确定编辑按钮"], "id", page_wode_xiugai_element["性别栏"]) #确定更改

        self.assertEqual(t1.strip(),get_element_text(self.driver, "id", page_wode_xiugai_element["性别栏"]).strip())

        print("改性别完毕")

        find_click_page(self.driver, "id", page_wode_xiugai_element["个人简介栏"], "id",page_wode_xiugai_element["内容编辑框"])  # 点击简介

        find(self.driver, "id", page_wode_xiugai_element["内容编辑框"]).set_text("333222111") #改成这样

        t1 = get_element_text(self.driver, "id", page_wode_xiugai_element["内容编辑框"])

        find_click_page(self.driver, "id", page_wode_xiugai_element["确定编辑按钮"], "id",page_wode_xiugai_element["个人简介栏"])  # 点击确定

        self.assertEqual(t1.strip(),get_element_text(self.driver, "id", page_wode_xiugai_element["个人简介栏"]).strip())

        print("改简介完毕")

        find_click_page(self.driver, "id", page_wode_xiugai_element["真实姓名栏"], "id",page_wode_xiugai_element["内容编辑框"]) #点击真名更改

        find(self.driver, "id", page_wode_xiugai_element["内容编辑框"]).set_text("superman")  # 改成这样

        t1 = get_element_text(self.driver, "id", page_wode_xiugai_element["内容编辑框"])

        find_click_page(self.driver, "id", page_wode_xiugai_element["确定编辑按钮"], "id", page_wode_xiugai_element["真实姓名栏"])  # 点击确定

        self.assertEqual(t1.strip(), get_element_text(self.driver, "id", page_wode_xiugai_element["真实姓名栏"]).strip())

        print("改真实名字完毕")

        find_click_page(self.driver, "id", page_wode_xiugai_element["年龄栏"], "id",page_wode_xiugai_element["内容编辑框"])  # 点击年龄更改

        find(self.driver, "id", page_wode_xiugai_element["内容编辑框"]).set_text("99")  # 改成这样

        t1 = get_element_text(self.driver, "id", page_wode_xiugai_element["内容编辑框"])

        find_click_page(self.driver, "id", page_wode_xiugai_element["确定编辑按钮"], "id",page_wode_xiugai_element["年龄栏"])  # 点击确定

        self.assertEqual(t1.strip(), get_element_text(self.driver, "id", page_wode_xiugai_element["年龄栏"]).strip())

        print("改年龄完毕")

        find_click_page(self.driver, "id", page_wode_xiugai_element["保存按钮"], "id", page_wode_xiugai_element["保存按钮"]) #点击保存

        find_click_page(self.driver, "zb", [(42, 75)], "id", page_wode_element["我的收藏按钮"])#返回

        print("测试个人信息更改完毕")

    @getImage
    def test007_page_wode_shoucan(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id", page_wode_element["我的收藏按钮"])  # 我的

        find_click_text(self.driver, "id", page_wode_element["我的收藏按钮"], "id",page_wode_shoucang_element["我的收藏标题栏"])  # 我的收藏
        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):
            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
            find_click_page(self.driver, "id", page_zuopin_element["作品详情-收藏/取消收藏"], "id",page_zuopin_element["作品详情-作品名"])
            t1 = get_element_text(self.driver, "id", page_zuopin_element["作品详情-作品名"])
            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id", page_wode_shoucang_element["我的收藏标题栏"]) #返回
            if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):
                self.assertNotEqual(t1.strip(),get_element_text(self.driver, "id", page_zuopin_element["作品列表-作品名"],"作品依然在收藏列表").strip())
            else:
                assertPage(self.driver, "id", page_wode_shoucang_element["没有内容图片"])
                print(" 列表为空")

        else:
            assertPage(self.driver,"id",page_wode_shoucang_element["没有内容图片"])
            print(" 列表为空")
        print("我的-收藏测试完毕")

    @getImage
    def test008_page_wode_zuopin(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id", page_wode_element["我的作品按钮"])#我的

        find_click_text(self.driver, "id", page_wode_element["我的作品按钮"], "id", page_wode_zuopin_element["我的作品标题栏"]) #我的作品
        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):
            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
            find_click_page(self.driver, "id",page_zuopin_element["作品详情-返回按钮"], "id", page_wode_zuopin_element["我的作品标题栏"]) #返回
        else:
            assertPage(self.driver,"id",page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")

        find_click_page(self.driver, "id", page_wode_zuopin_element["已发布页签"], "id", page_wode_zuopin_element["我的作品标题栏"])#已发布
        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):
            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id", page_wode_zuopin_element["我的作品标题栏"]) #返回
        else:
            assertPage(self.driver, "id", page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")
        print("我的作品-已发布测试完毕")


        find_click_page(self.driver, "id", page_wode_zuopin_element["未发布页签"], "id", page_wode_zuopin_element["我的作品标题栏"])  # 未发布
        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):
            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])
            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id", page_wode_zuopin_element["我的作品标题栏"]) #返回
        else:
            assertPage(self.driver, "id", page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")
        print("我的作品-未发布测试完毕")

        find_click_text(self.driver, "zb", [(42,75)], "id", page_wode_element["我的收藏按钮"])#返回
        print("我的作品测试完毕")

    @getImage
    def test009_fabu(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id",page_wode_element["我的作品按钮"])  # 我的
        find_click_text(self.driver, "id", page_wode_element["我的作品按钮"], "id", page_wode_zuopin_element["我的作品标题栏"]) #我的作品

        find_click_page(self.driver, "id", page_wode_zuopin_element["未发布页签"], "id", page_wode_zuopin_element["我的作品标题栏"]) # 未发布
        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):
            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])

            find_click_text(self.driver, "id", page_fabu_element["发布按钮"], "id", page_fabu_element["发布按钮"]) #点击发布

            find(self.driver, "x", "//android.widget.TextView[contains(@text,'动作')]").click()  # 标签有很多这是其中一个

            find(self.driver, "x", "//android.widget.TextView[contains(@text,'冒险')]").click() #标签有很多这是其中一个

            find(self.driver, "x", "//android.widget.TextView[contains(@text,'模拟')]").click()  # 标签有很多这是其中一个

            find(self.driver, "x", "//android.widget.TextView[contains(@text,'RPG')]").click()  # 标签有很多这是其中一个

            find_click_page(self.driver, "id", page_fabu_element["发布按钮"], "id", page_zuopin_element["作品详情-作者栏"]) #确认发布
            print("发布成功")
            t1 = get_element_text(self.driver,"id",page_zuopin_element["作品详情-作品名"])

            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id", page_wode_zuopin_element["我的作品标题栏"]) #返回

            find_click_page(self.driver, "id", page_wode_zuopin_element["已发布页签"], "id", page_zuopin_element["作品列表-作品框"])#进入已发布

            self.assertEqual(t1.strip(),get_element_text(self.driver,"id",page_zuopin_element["作品列表-作品名"]).strip()) #判断是否已经在已发布列表中

            find_click_page(self.driver, "zb", [(42, 75)], "id", page_wode_element["我的收藏按钮"])#返回

            find_click_page(self.driver, "id", page_one_element["游戏按钮"], "id",page_one_element["创作按钮"])  #回到首页

            find_click_page(self.driver, "id", page_one_element["最新页签"], "id", page_zuopin_element["作品列表-作品框"]) #进入最新
            self.assertEqual(t1.strip(),get_element_text(self.driver, "id", page_zuopin_element["作品列表-作品名"]).strip())  # 判断是否已经在已发布列表中

            print("发布测试完毕")

        else:
            assertPage(self.driver, "id", page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")

    @getImage
    def test010_xiugaifabu(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id",page_wode_element["我的作品按钮"])  # 我的
        find_click_text(self.driver, "id", page_wode_element["我的作品按钮"], "id", page_wode_zuopin_element["我的作品标题栏"])  # 我的作品

        find_click_page(self.driver, "id", page_wode_zuopin_element["已发布页签"], "id", page_wode_zuopin_element["我的作品标题栏"]) # 已发布

        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):

            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id", page_zuopin_element["作品详情-作品名"])

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["作品编辑"], "id", page_zuopin_xiugai_element["修改"])#点击编辑

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["修改"], "id", page_zuopin_xiugai_element["更换封面"])#选择修改

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["更换封面"], "id",page_zuopin_xiugai_element["图片"])  # 点击封面

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["图片选择"], "id", page_zuopin_xiugai_element["图片"])  # 选头像

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["选择完成按钮"], "id", page_zuopin_xiugai_element["更换封面"])  # 完成

            print("封面修改完毕")

            find(self.driver, "id", page_zuopin_xiugai_element["更改名字"]).set_text("very666")

            find(self.driver, "id", page_zuopin_xiugai_element["更改简介"]).set_text("SO666666!!")

            self.driver.hide_keyboard()   #收起键盘

            print("名字和简介修改完毕")

            t1 = get_element_text(self.driver, "id", page_zuopin_element["作品详情-作品名"])

            find_click_page(self.driver, "id",page_fabu_element["发布按钮"], "id", page_zuopin_xiugai_element["作品编辑"])  # 点击发布

            self.assertEqual(t1.strip(), get_element_text(self.driver, "id", page_zuopin_element["作品详情-作品名"]).strip())

            print("修改发布成功")

            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id", page_wode_zuopin_element["我的作品标题栏"])

            self.assertEqual(t1.strip(), get_element_text(self.driver, "id", page_zuopin_element["作品列表-作品名"]).strip())#判断是否已经在已发布列表中修改成功

            find_click_page(self.driver, "zb", [(42, 75)], "id", page_wode_element["我的收藏按钮"])  # 返回

            find_click_page(self.driver, "id", page_one_element["游戏按钮"], "id",page_one_element["创作按钮"])  # 回到首页

            find_click_page(self.driver, "id", page_one_element["最新页签"], "id",page_zuopin_element["作品列表-作品框"])  # 进入最新
            self.assertEqual(t1.strip(),get_element_text(self.driver, "id", page_zuopin_element["作品列表-作品名"]).strip())  # 判断是否已经在已发布列表中

            print("发布修改测试完毕")

        else:
            assertPage(self.driver, "id", page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")

    @getImage
    def test011_qxfabu(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id",page_wode_element["我的作品按钮"])  # 我的
        find_click_text(self.driver, "id", page_wode_element["我的作品按钮"], "id", page_wode_zuopin_element["我的作品标题栏"])  # 我的作品

        find_click_page(self.driver, "id", page_wode_zuopin_element["已发布页签"], "id", page_wode_zuopin_element["我的作品标题栏"])  # 已发布发布

        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):

            find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["作品编辑"], "id", page_zuopin_xiugai_element["取消发布"])  # 点击编辑

            find_click_page(self.driver, "id", page_zuopin_xiugai_element["取消发布"], "id", page_fabu_element["取消发布提示框"]) #点击取消

            find_click_page(self.driver, "id", page_fabu_element["确定按钮"], "id", page_fabu_element["发布按钮"]) #确定取消发布

            t1 = get_element_text(self.driver, "id", page_zuopin_element["作品详情-作品名"])

            find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id",page_wode_zuopin_element["我的作品标题栏"])  # 返回

            find_click_page(self.driver, "id", page_wode_zuopin_element["未发布页签"], "id", page_zuopin_element["作品列表-作品框"]) #点击未发布

            self.assertEqual(t1.strip(),get_element_text(self.driver, "id", page_zuopin_element["作品列表-作品名"]).strip())

            print("取消发布测试完毕")

        else:
            assertPage(self.driver, "id", page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")

    @getImage
    def test012_shanczuopin(self):

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id",page_wode_element["我的作品按钮"])  # 我的
        find_click_text(self.driver, "id", page_wode_element["我的作品按钮"], "id",page_wode_zuopin_element["我的作品标题栏"])  # 我的作品

        find_click_page(self.driver, "id", page_wode_zuopin_element["未发布页签"], "id", page_wode_zuopin_element["我的作品标题栏"])  # 未发布

        if element_exist(self.driver, "id", page_zuopin_element["作品列表-作品框"]):

            find_click_page(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id", page_fabu_element["删除作品按钮"])

            t1 = get_element_text(self.driver, "id", page_zuopin_element["作品详情-作品名"])

            find_click_page(self.driver, "id", page_fabu_element["删除作品按钮"], "id", page_fabu_element["取消发布提示框"]) #点击删除

            find_click_page(self.driver, "id", page_fabu_element["取消按钮"], "id", page_fabu_element["删除作品按钮"]) # 点击取消

            find_click_page(self.driver, "id", page_fabu_element["删除作品按钮"], "id", page_fabu_element["取消发布提示框"]) #点击删除

            find_click_page(self.driver, "id", page_fabu_element["确定按钮"], "id", page_wode_zuopin_element["未发布页签"])#点击确定删除

            self.assertNotEqual(t1.strip(),get_element_text(self.driver, "id", page_zuopin_element["作品列表-作品名"],"作品依然再未发布列表").strip())

            print("删除作品测试完毕")

        else:
            assertPage(self.driver, "id", page_wode_zuopin_element["没有内容图片"])
            print(" 列表为空")

    @getImage
    def test013_gerenye(self): #他人的个人主页

        find_click_page(self.driver, "id", page_one_element["游戏按钮"], "id", page_one_element["首页标题栏"])  # 推荐
        find_click_text(self.driver, "id", page_zuopin_element["作品列表-作品名"], "id",page_zuopin_element["作品详情-作品名"])

        find_click_text(self.driver, "id",page_zuopin_element["作品详情-作者名"], "id", page_personal_element["作者名"]) #点击作者进入主页

        find_click_page(self.driver, "id", page_personal_element["返回按钮"], "id", page_zuopin_element["作品详情-作者名"]) #返回详情

        find_click_page(self.driver, "id", page_zuopin_element["作品详情-返回按钮"], "id", page_one_element["首页标题栏"])  # 返回

        print("个人主页测试完毕")

    @getImage
    def test014_chuangzuo(self): #直接进入创作页面
        '''
        H5,不好弄
        '''

        find_click_page(self.driver, "id", page_one_element["视频按钮"], "id", page_one_element["创作按钮"])

        find_click_page(self.driver, "id", page_one_element["视频-公开课按钮"], "id", page_one_element["创作按钮"])

        find_click_page(self.driver, "id", page_one_element["游戏按钮"], "id", page_one_element["创作按钮"])

        find(self.driver, "id", page_one_element["创作按钮"]).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_accessibility_id("事件").click()
        self.driver.press_keycode(4)


        print("可进入创作页面")

    @getImage
    def test015_logout(self): #退出登录

        find_click_page(self.driver, "id", page_one_element["我的按钮"], "id",page_wode_element["个人信息编辑按钮"])  # 我的

        find_click_page(self.driver, "id", page_wode_element["退出登录按钮"], "id",page_wode_element["退出弹窗标题栏"])  # 退出

        find_click_page(self.driver, "id", page_wode_element["退出按钮"], "id", page_wode_element["头像按钮"])

        print("退出登录测试完毕")

    @getImage
    def test016_chuangjian_login(self): #通过创作登录

        find(self.driver, "id", page_one_element["创作按钮"]).click()
        find_click_text(self.driver, "id", page_login_element["登录按钮"], "id", page_login_element["确认登录按钮"])
        find(self.driver, "id", page_login_element["帐号输入框"]).send_keys(account["测试服帐号1"])
        find(self.driver, "id", page_login_element["密码输入框"]).send_keys(account["测试服密码1"])
        find(self.driver, "id", page_login_element["确认登录按钮"]).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_accessibility_id("事件").click()
        self.driver.press_keycode(4)
        print("创作登录测试完毕")

def all_case(): #全用例
    case_path = getpath()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

    print(discover)
    return discover

def suite_case(): #部分用例

     suite = unittest.TestSuite()
     #suite.addTest(testCodemao("test015_logout"))
     suite.addTest(testCodemao("test004_fenxiang"))
     return suite

if __name__ == '__main__':

    #unittest.main()
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("自动化测试开始:",now )

    # 2、html报告文件路径
    path = reportpath()
    report_abspath = os.path.join(path, "result_" + now + ".html")

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告,测试结果如下：',description=u'用例执行情况：')

    # 4、调用add_case函数返回值
    runner.run(suite_case())
    fp.close()
    end = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("自动化测试结束:",end)



