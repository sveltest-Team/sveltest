#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/10/17


from win10toast import ToastNotifier
import _thread
from time import sleep
from typing import Optional,Sequence,Union


"""
win10toast 的库底层为win32api、win32con和win32gui
"""

toaster = ToastNotifier()


def show_toast(title,msg):
    toaster.show_toast(title=title,
                       msg=msg,
                       icon_path=None,
                       duration=10,
                       threaded=True
                       )


def toast_send(title:Sequence[str],msg:Optional[str]=None):
    _thread.start_new_thread(show_toast, (title,msg))
    sleep(0.1)



def test_toast(count:Union[str,int]=0,
               pass_count:Union[str,int]=0,
               error_count:Union[str,int]=0,
               fail_count:Union[str,int]=0,
               skip_count:Union[str,int]=0,
               ):
    toast_send(title="sveltest-测试执行结果",msg=f"""
    你本次执行的测试用例数为 {count} 条，其具体结果如下：
    通过 {pass_count}条，失败 {fail_count}条，
    异常 {error_count}条，跳过 {skip_count}条，
    """)

if __name__ == '__main__':
    test_toast()


