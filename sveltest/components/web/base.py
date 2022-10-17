#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sveltest.bin.conf import settings
from selenium.webdriver import ActionChains
import datetime
from sveltest.components.web.sume import WEBDRIVER_ELEMENT



base_url = ""

class WebDriverBase:
    """Page 封装的是公共类 所有测试类都基于该基类"""
    # Page encapsulates a common class. All test classes are based on that base class.
    def __init__(self,driver,path=None,timeout=10):
        """
        :param driver:
        :param timeout:
        :param path:


        """

        self.driver = driver
        # 加启动配置
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')


        if not settings.WEBDRIVER_TEST_SETTINGS:
            #全局元素定位等待
            self.driver.implicitly_wait(time_to_wait=settings.WEBDRIVER_TEST_SETTINGS["GLOBAL_IMPLICITLY_WAIT"])
        else:
            self.driver.implicitly_wait(time_to_wait=timeout)

        self.open(path)


    def option(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        return option

    def open(self,path=None):
        """

        :param path:
        :return:
        """

        url = path if path else base_url

        return self.driver.get(url=url)


    def quit(self):
        """

        :return:
        """
        return self.driver.quit()






# Map PageElement constructor arguments to webdriver locator enums
LOCATOR_LIST = {
    # selenium
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,

    # appium
    # 'ios_uiautomation': MobileBy.IOS_UIAUTOMATION,
    # 'ios_predicate': MobileBy.IOS_PREDICATE,
    # 'ios_class_chain': MobileBy.IOS_CLASS_CHAIN,
    # 'android_uiautomator': MobileBy.ANDROID_UIAUTOMATOR,
    # 'android_viewtag': MobileBy.ANDROID_VIEWTAG,
    # 'android_datamatcher': MobileBy.ANDROID_DATA_MATCHER,
    # 'accessibility_id': MobileBy.ACCESSIBILITY_ID,
    # 'image': MobileBy.IMAGE,
    # 'custom': MobileBy.CUSTOM,
}


class PageBaseObject(WebDriverBase):
    def __init__(self,driver,path=None,timeout=10):
        """

        :param driver:
        :param path:
        :param timeout:
        """
        super(PageBaseObject, self).__init__(driver,path=path,timeout=timeout)



    def page_(self,by,element,timeout=5,pall=0.5,describe=None):
        """

        :param by:
        :param element:
        :param timeout:
        :param pall:
        :param describe:
        :return:
        """
        describe = describe
        bys = by
        if by == by:
            return self.webWait(
                by=(WEBDRIVER_ELEMENT[by], element),
                timeout=timeout,
                pall=pall
            )
        else:
            pass

    def input(self,by,element,value,timeout=5,pall=0.5,describe=None):
        """
        :param driver:
        :param By:
        :param element:
        :param valuse:
        :param describe:
        :return:
        """
        describe = describe
        bys = by
        if by == by:
            return self.webWait(
                by=(WEBDRIVER_ELEMENT[by],element),
                timeout=timeout,
                pall=pall
            ).send_keys(value)


    def webWait(self,by, timeout=5, pall=0.5):
        """
        driver 浏览器实例对象
        timeout 等待的实际时间
        poll 刷新间隔
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout, pall).until(
                # 直到被定位的元素被找到
                exp.presence_of_element_located(by)
            )
            return element
        except:
            print("元素定位失败,你可以尝试修改下 %s" % str(by))


    def click(self,by,element,timeout=5,pall=0.5,describe=None):
        describe = describe
        bys = by
        if by == by:
            return self.webWait(
                by=(WEBDRIVER_ELEMENT[by], element),
                timeout=timeout,
                pall=pall
            ).click()
        else:
            pass


class WebActon(PageBaseObject):

    def __init__(self,driver,path,timeout):
        super(WebActon, self).__init__(driver, path=path, timeout=timeout)
        self.page_source = self._page_source()
        self.title = self._title()
        self.url = self._current_url()

    def max_window(self):
        """

        :return:
        """
        return self.driver.maximize_window()
    def min_window(self):
        """

        :return:
        """
        return self.driver.minimize_window()

    def size_window(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        return self.driver.set_window_size(x, y)


    def shot_save(self,path,name=None):
        try:
            if name:
                pr = os.path.join(path, name + '.png')
            else:
                sr = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                pr = os.path.join(path, sr + '.png')
            self.driver.save_screenshot(pr)
            return True
        except Exception as e:
            return e

    # def shot_base64_save(self,path):
    #     try:
    #         sr = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    #         pr = path + '\\' + sr + '.png'
    #         self.driver.get_screenshot_as_png(pr)
    #         print('截图成功！！！')
    #     except Exception:
    #         print('截图失败！！！')

    def handles(self):
        return self.driver.window_handles

    def current_handle(self):
        return self.driver.current_window_handle

    def switch_windows(self,index):
        return self.driver.switch_to.window(index)

    def scrollTo(self,top,bottom):
        js = "window.scrollTo(%s,%s);"%(top,bottom)
        return self.driver.execute_script(js)

    def _page_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def _title(self):
        return self.driver.title

    def _current_url(self):
        return self.driver.current_url

    def select_(self,by,element,timeout=5,pall=0.5,mode=("all",None)):
        from selenium.webdriver.support.ui import Select
        if mode[0] == "all":
            if by == by:
                select_element = self.webWait(by=(WEBDRIVER_ELEMENT[by], element), timeout=timeout, pall=pall)
                all_options = select_element.find_elements_by_tag_name("option")
                return all_options
        elif mode[0] == "index":
            select = Select(self.webWait(by=(WEBDRIVER_ELEMENT[by],element),timeout=timeout,pall=pall))
            select.select_by_index(mode[1])

        elif mode[0] == "text":
            select = Select(self.webWait(by=(WEBDRIVER_ELEMENT[by],element),timeout=timeout,pall=pall))
            select.select_by_visible_text(mode[1])

        elif mode[0] == "value":
            select = Select(self.webWait(by=(WEBDRIVER_ELEMENT[by],element),timeout=timeout,pall=pall))
            select.select_by_value(mode[1])

    def deselect_all(self,by,element,timeout=5,pall=0.5):
        """取消使用选择的选项"""
        from selenium.webdriver.support.ui import Select
        select = Select(self.webWait(by=(WEBDRIVER_ELEMENT[by],element),timeout=timeout,pall=pall))
        select.deselect_all()

    def select_options(self,by,element,timeout=5,pall=0.5):
        """获取所有可选择的选项"""
        from selenium.webdriver.support.ui import Select
        select = Select(self.webWait(by=(WEBDRIVER_ELEMENT[by],element),timeout=timeout,pall=pall))
        return select.options


    def drag_and_drop(self,start,end):
        """拖拽"""

        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.page_(start[0],start[1]), self.page_(end[0],end[1]))
        # 执行
        actions.perform()

    def drag_offset(self,start,x,y):
        """按照坐标 拖拽"""

        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(source=self.page_(start[0],start[1]),xoffset=x,yoffset=y)
        # 执行
        actions.perform()


    def get_window_handle(self,all=False):
        """获取当前窗口句柄"""
        if all is True:
            return self.driver.window_handles
        else:
            return self.driver.current_window_handle

    def to_window(self,handle):
        """切换到指定的窗口"""
        return self.driver.switch_to.window(handle)


class PageBase(WebActon):
    """

    """
    def __init__(self,driver,path=None,timeout=5):
        """

        """
        super(PageBase, self).__init__(driver,path,timeout)







