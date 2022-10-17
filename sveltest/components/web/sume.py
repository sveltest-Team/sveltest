#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/6/17
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


WEBDRIVER_ELEMENT = {
    'css': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
}


Keys_Home = Keys.HOME #按下Home键

Keys_Back_Space = Keys.BACK_SPACE #删除键（BackSpace）

Keys_Space = Keys.SPACE #空格键(Space)

Keys_Tab = Keys.TAB #制表键(Tab)

Keys_Escape =  Keys.ESCAPE #回退键（Esc）

Keys_Enter = Keys.ENTER # 回车键（Enter）

Keys_Ctrl_A = (Keys.CONTROL,'a') #全选

Keys_Ctrl_C = (Keys.CONTROL,'c') #复制（Ctrl+C）

Keys_Ctrl_X = (Keys.CONTROL,'x') #剪切（Ctrl+X）

Keys_Ctrl_V = (Keys.CONTROL,'v') #粘贴（Ctrl+V）



# send_keys(Keys.F1) 键盘F1
# ……
# Send_keys(Keys.F5)键盘F5
# …
# send_keys(Keys.F12) 键盘F12
