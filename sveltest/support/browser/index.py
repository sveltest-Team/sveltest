#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sveltest.support.logger_v2 import log_v2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def head():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument(
        'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')
    return chrome_options


def get_browser_version(driver="chrome",options=head()):



    if driver == "geckodriver" or driver == "Firefox" or driver == "hf":
        log_v2.info("正在获取本地安装 Firefox 浏览器的版本号...")
        driver = webdriver.Firefox(options=options)

    else:
        log_v2.info("正在获取本地安装 Chrome 浏览器的版本号...")
        driver = webdriver.Chrome(options=options)

    info = driver.capabilities.get('chrome').get("chromedriverVersion").split(' ')
    log_v2.info("版本号获取成功！版本为："+info[0])
    driver.quit()
    return info


