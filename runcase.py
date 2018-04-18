#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from testcase import *

def all_case(): #全用例
    case_path = getpath()
    #case_path = lambda:os.path.join(os.getcwd())
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

    print(discover)
    return discover

def suite_case(): #部分用例

     suite = unittest.TestSuite()
     suite.addTest(testCodemao("test000_login"))
     #suite.addTest(testCodemao("test005_page_wode"))
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
    runner.run(suite_case())  #参数为选择全部还是选择单独
    fp.close()
    end = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("自动化测试结束:",end)