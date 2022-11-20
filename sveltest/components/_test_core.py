import os
import functools
import unittest

from sveltest.components.dblib import ShelveBase


def rely(case_name:str=None):
    """
    :param case
    :return:
    """
    def wrapper_case(test_func):

        @functools.wraps(test_func)
        def _func(cur):

            if case_name == test_func.__name__:
                raise ValueError("{} 你不能将依赖作为自己".format(case_name))

            failures = [str(fail_[0]).split("=")[0].split(" ")[0] for fail_ in cur._outcome.result.failures]

            errors = [str(fail_[0]).split("=")[0].split(" ")[0] for fail_ in cur._outcome.result.errors]

            skipped = [str(fail_[0]).split("=")[0].split(" ")[0] for fail_ in cur._outcome.result.skipped]

            tag_status = (case_name in failures) or (case_name in errors) or (case_name in skipped)

            test = unittest.skipIf(tag_status, '{} ({} rely {})'.format(test_func.__name__,test_func.__name__,case_name))(test_func)
            return test(cur)
        return _func
    return wrapper_case


import inspect

def env(arg=None,**kwargs):
    def func(cls):
        def wrapper(**kwargs):

            if kwargs:
                from sveltest.support.common import ObjectDict
                print(cls.__name__)

                kw = ObjectDict(kwargs)
                cls.cls_name = cls.__name__

                try:
                    from sveltest.bin.conf import settings
                    cls.obj_conf = ObjectDict(settings.ENVIRONMENT_CLASSES_CONFIG)
                except:
                    pass

                cls.env =  cls.obj_conf.DEFAULT_ENVIRONMENT_NAME

                try:
                    #:todo 暂时不进行该逻辑处理，后面版本将完善
                    # if settings.DEBUG:
                    #      cls.ENV_CLASS = "ENVIRONMENT_CLASS_DEV"
                    # else:
                    #     cls.ENV_CLASS = "ENVIRONMENT_CLASS_PROD"


                    cls.frontend_env_name = cls.obj_conf.FRONTEND
                    cls.backend_env_name = cls.obj_conf.BACKEND
                    if cls.env == "dev": cls.ENV_CLASS = "ENVIRONMENT_CLASS_DEV"
                    if cls.env == "sit": cls.ENV_CLASS = "ENVIRONMENT_CLASS_SIT"
                    if cls.env == "uat": cls.ENV_CLASS = "ENVIRONMENT_CLASS_UAT"
                    if cls.env == "prod": cls.ENV_CLASS = "ENVIRONMENT_CLASS_PROD"


                    cls.env_frontend_info = ObjectDict(cls.obj_conf.FRONTEND[cls.ENV_CLASS])
                    cls.env_backend_info = ObjectDict(cls.obj_conf.BACKEND[cls.ENV_CLASS])


                    cls.env_backend_port = cls.env_backend_info.ENVIRONMENT_PORT

                    cls.env_backend_host = cls.env_backend_info.ENVIRONMENT_HOST

                    if not cls.env_backend_info:
                        cls.env_backend_network_protocol = cls.env_backend_info.NETWORK_PROTOCOL
                    else:
                        raise Exception("请将 ENVIRONMENT_CLASSES_CONFIG 配置完整")


                    cls.env_frontend_port = cls.env_frontend_info.ENVIRONMENT_PORT
                    cls.env_frontend_host = cls.env_frontend_info.ENVIRONMENT_HOST
                    cls.env_frontend_network_protocol = cls.env_frontend_info.NETWORK_PROTOCOL

                    if  cls.env_frontend_network_protocol =="http" : protocol = "http://"
                    if  cls.env_frontend_network_protocol =="https" : protocol = "https://"
                    if  cls.env_frontend_network_protocol =="ws" : protocol = "ws://"
                    if  cls.env_frontend_network_protocol =="wss" : protocol = "wss://"

                    url_ = ''.join([protocol,cls.env_frontend_host])
                    if cls.env_frontend_port is not None and cls.env_frontend_port!="":
                        cls.frontend_host = ":".join([url_,str(cls.env_frontend_port)])
                    else:
                        cls.frontend_host = url_


                    try:
                        url_end = ''.join([protocol,cls.env_backend_host])
                        if cls.env_backend_port is not None and cls.env_backend_port!="":
                            cls.backend_host = ":".join([url_end,str(cls.env_backend_port)])
                        else:
                            cls.backend_host = url_end
                    except:
                        cls.backend_host = None


                except:
                    cls.current_env_host = cls.obj_conf.ENVIRONMENT_HOST if cls.obj_conf.ENVIRONMENT_HOST else "80"
                    cls.current_env_port = cls.obj_conf.ENVIRONMENT_PORT

                return cls


        return wrapper(**kwargs)

    return func(arg) if inspect.isclass(arg) else func



def request_env(arg=None,**kwargs):
    def func(cls):

        def wrapper(**kwargs):
            from sveltest.support.common import ObjectDict

            cls.params = ObjectDict(kwargs)

            cls.cls_name = cls.__name__


            try:
                from sveltest.bin.conf import settings

                cls.obj_conf = ObjectDict(settings.ENVIRONMENT_CLASSES_CONFIG)
            except:
                pass

            cls.env =  cls.obj_conf.DEFAULT_ENVIRONMENT_NAME
            cls.env_headers =  cls.obj_conf.HEADERS

            if cls.env == "dev": cls.ENV_CLASS = "ENVIRONMENT_DEV_HOST"
            if cls.env == "sit": cls.ENV_CLASS = "ENVIRONMENT_SIT_HOST"
            if cls.env == "uat": cls.ENV_CLASS = "ENVIRONMENT_UAT_HOST"
            if cls.env == "prod": cls.ENV_CLASS = "ENVIRONMENT_PROD_HOST"

            cls.info = ObjectDict(cls.obj_conf)
            cls.env_ = ObjectDict(cls.info.FRONTEND)


            # try:
            #     #:todo 暂时不进行该逻辑处理，后面版本将完善
            #     # if settings.DEBUG:
            #     #      cls.ENV_CLASS = "ENVIRONMENT_CLASS_DEV"
            #     # else:
            #     #     cls.ENV_CLASS = "ENVIRONMENT_CLASS_PROD"
            #
            #
            cls.frontend_env_host = cls.env_[cls.ENV_CLASS]

            cls.backend_env_host = cls.env_[cls.ENV_CLASS]
            # print( bool(cls.env_headers))
            cls.Header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            }

            pub = ShelveBase()
            if pub.get("token", ):
                cls.token_ = cls.Header.update(pub.get("token", ))
                pub.quit()

            if bool(cls.env_headers) :
                cls.Header = cls.env_headers

            else:
                if cls.cls_name.upper() in ["POST", "PUT", "PATCH"]:

                    cls.Header.update({
                        'accept': "application/json", "Content-Type": "application/json",

                    })
            return cls
        return wrapper(**kwargs)

    return func(arg) if inspect.isclass(arg) else func



# http://www.66ip.cn/pt.html
# 代理器
# def proxy(=None,**kwargs):
#
#     def func(cls):
#
#         def wrapper(*args, **kwargs):
#             print('获取关键字参数的dict', kwargs)
#             return cls(*args, **kwargs)
#         return wrapper
#     return func


proxy_manager=["https://proxy.ip3366.net/doc/putong/"]



