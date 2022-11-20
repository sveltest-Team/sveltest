#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/10/20

import json
import requests
from typing import Optional, List, Union, Sequence, Dict, overload, Tuple
from sveltest.bin.conf.application import app_loader
from sveltest.components._test_core import (request_env)
from sveltest.support.common import ObjectDict
from sveltest.bin.conf import settings
from sveltest.components.dblib import ShelveBase

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# 代理池 Agent Pool

data_cache = ShelveBase()
# 内置环境控制
class RequestBase(object):

    auth_class = ObjectDict(settings.AUTH_VALIDATORS)
    environment_class = ObjectDict(settings.ENVIRONMENT_CLASSES_CONFIG)


    def __init__(self):

        self.encoding = None


    def get_auth_class(self):
        if self.auth_class.CLASS:
            cached_ = app_loader.component(self.auth_class.CLASS)
            setattr(self,"cache_",cached_)


    def get(self, router: Optional[str],
            data: Optional[Dict]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Optional[bool]=False,
            env_control:Optional[bool]=True,
            allow_redirects:Optional[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            is_backend:Optional[bool]=False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """

        self.env_info = self.__env(self.get)
        _rh = dict(self.env_info.Header)
        __get_ = self.__get_auth_()

        try:
            if __get_:
                _rh.update(__get_)
            else:
                _rh.update(self.cache_)
        except:
            pass



        if headers is False:
            self.headers_data = _rh

        else:
            _rh.update(headers)
            self.headers_data = _rh



        if router and env_control is True:
            self.__request_module = requests.get(
                url=self._join([self.env_info.backend_env_host if is_backend  else self.env_info.frontend_env_host
                                   ,router]), params=data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects, timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.get(
                url=router, params=data, proxies=proxies, verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self


    def post(self, router: Optional[str],
            data: Optional[Union[Dict,open]]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Optional[bool]=False,
            env_control:bool=True,
            is_backend: Optional[bool] = False,
            allow_redirects:Optional[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """
        self.env_info = self.__env(self.post)

        _rh = dict(self.env_info.Header)
        __get_ = self.__get_auth_()

        try:
            if __get_:
                _rh.update(__get_)
            else:
                _rh.update(self.cache_)
        except:
            pass

        if headers is False:
            self.headers_data = _rh

        else:
            _rh.update(headers)
            self.headers_data = _rh



        try:
            _req_data = json.dumps(data) if self.headers_data["Content-Type"] == "application/json" else data

        except:
            _req_data = data

        if router and env_control is True:
            self.__request_module = requests.post(
                url=self._join([self.env_info.backend_env_host if is_backend  else self.env_info.frontend_env_host
                                   ,router]), data=_req_data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects,
                timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.post(
                url=router, data=_req_data, proxies=proxies,
                verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self




    def upload_file(self,file:Optional[Union[List[str],str]],type:Optional[str]="image/png"):
        """
        上传文件
        """
        if isinstance(file,str):
            with open('massive-body', 'rb') as f:
                self.post('http://some.url/streamed', data=f)

        if isinstance(file,list):

            multiple_files = [
                ('images', (x.replace("\\","/").split("/")[-1], open(x, 'rb'), 'image/png'))
                for x in file
            ]
            requests.post('url', files=multiple_files)

        return self



    def put(self, router: Optional[str],
            data: Optional[Union[Dict,open]]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Optional[bool]=False,
            is_backend: Optional[bool] = False,
            env_control:bool=True,
            allow_redirects:Optional[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """

        self.env_info = self.__env(self.put)

        _rh = dict(self.env_info.Header)
        __get_ = self.__get_auth_()

        try:
            if __get_:
                _rh.update(__get_)
            else:
                _rh.update(self.cache_)
        except:
            pass

        if headers is False:
            self.headers_data = _rh

        else:
            _rh.update(headers)
            self.headers_data = _rh



        try:
            _req_data = json.dumps(data) if self.headers_data["Content-Type"] == "application/json" else data

        except:
            _req_data = data

        if router and env_control is True:
            self.__request_module = requests.put(
                url=self._join([self.env_info.backend_env_host if is_backend  else self.env_info.frontend_env_host
                                   ,router]), data=_req_data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects,
                timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.put(
                url=router, data=_req_data, proxies=proxies,
                verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self

    @request_env()
    def patch(self, router: Optional[str],
            data: Optional[Union[Dict,open]]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Optional[bool]=False,
            env_control:bool=True,
            is_backend: Optional[bool] = False,
            allow_redirects:Optional[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """


        self.env_info = self.__env(self.patch)

        _rh = dict(self.env_info.Header)
        __get_ = self.__get_auth_()

        try:
            if __get_:
                _rh.update(__get_)
            else:
                _rh.update(self.cache_)
        except:
            pass


        if headers is False:
            self.headers_data = _rh

        else:
            _rh.update(headers)
            self.headers_data = _rh



        try:
            _req_data = json.dumps(data) if self.headers_data["Content-Type"] == "application/json" else data

        except:
            _req_data = data

        if router and env_control is True:
            self.__request_module = requests.patch(
                url=self._join([self.env_info.backend_env_host if is_backend  else self.env_info.frontend_env_host
                                   ,router]), data=_req_data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects,
                timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.patch(
                url=router, data=_req_data, proxies=proxies,
                verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self




    @request_env()
    def delete(self, router: Optional[str],
            data: Optional[Dict]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Optional[bool]=False,
            env_control:Optional[bool]=True,
            allow_redirects:Optional[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            is_backend: Optional[bool] = False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """

        self.env_info = self.__env(self.delete)



        _rh = dict(self.env_info.Header)
        __get_ = self.__get_auth_()

        try:
            if __get_:
                _rh.update(__get_)
            else:
                _rh.update(self.cache_)
        except:
            pass


        if headers is False:
            self.headers_data = _rh

        else:
            _rh.update(headers)
            self.headers_data = _rh


        if router and env_control is True:
            self.__request_module = requests.delete(
                url=self._join([self.env_info.backend_env_host if is_backend  else self.env_info.frontend_env_host
                                   ,router]), params=data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects, timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.delete(
                url=router, params=data, proxies=proxies, verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self




    def code_ok(self):
        return requests.codes.ok


    @property
    def request_url(self):
        """

        """
        return self.__request_module.request.url

    @property
    def url(self):
        """

        """
        return self.__request_module.url



    def __get_auth_(self):
        """

        """
        if data_cache.get("token"):
            return data_cache.get("token")
        else:
            return False

    def _join(self, j:Optional[List]):
        """

        """
        return '/'.join(j)


    @property
    def content(self):
        """

        """
        return self.__request_module.content

    @property
    def text(self):
        """

        """

        return self.__request_module.text

    @property
    def json(self):
        """

        """
        return self.__request_module.json()


    def encoding_(self,coding:Optional[str]="utf-8"):
        """

        """
        self.__request_module.encoding = coding
        return self

    def save_image(self,content:Optional[bytes],fp:Optional[open]):
        """

        """
        from PIL import Image
        from io import BytesIO

        img = Image.open(BytesIO(content))
        img.save(fp=fp)
        return self

    @property
    def request_header(self):
        return HttpRequestHeaders(self.__request_module.request.headers)

    @property
    def request_headers(self):
        return self.__request_module.request.headers


    @property
    def header(self):
        """
        查看请求头
        """
        return HttpResponseHeaders(self.__request_module.headers)

    @property
    def headers(self):
        """
        查看请求头
        """
        return self.__request_module.headers


    @property
    def headers_obj(self):
        """
        查看请求头
        """
        return ObjectDict(self.__request_module.headers)

    @property
    def history(self):
        """
        查看请求头
        """
        return self.__request_module.history

    @property
    def status_code(self):
        """
        查看请求头
        """
        return self.__request_module.status_code

    def __env(self,cls_name:Optional[object]):
        """

        """
        self.cls_name = cls_name.__name__

        from sveltest.bin.conf import settings
        self.obj_conf = ObjectDict(settings.ENVIRONMENT_CLASSES_CONFIG)
        self.env = self.obj_conf.DEFAULT_ENVIRONMENT_NAME
        self.env_headers = self.obj_conf.HEADERS

        if self.env == "dev": self.ENV_CLASS = "ENVIRONMENT_DEV_HOST"
        if self.env == "sit": self.ENV_CLASS = "ENVIRONMENT_SIT_HOST"
        if self.env == "uat": self.ENV_CLASS = "ENVIRONMENT_UAT_HOST"
        if self.env == "prod": self.ENV_CLASS = "ENVIRONMENT_PROD_HOST"

        self.info = ObjectDict(self.obj_conf)
        self.env_ = ObjectDict(self.info.FRONTEND)

        # try:
        #     #:todo 暂时不进行该逻辑处理，后面版本将完善
        #     # if settings.DEBUG:
        #     #      cls.ENV_CLASS = "ENVIRONMENT_CLASS_DEV"
        #     # else:
        #     #     cls.ENV_CLASS = "ENVIRONMENT_CLASS_PROD"
        #
        #
        self.frontend_env_host = self.env_[self.ENV_CLASS]

        self.backend_env_host = self.env_[self.ENV_CLASS]
        # print( bool(cls.env_headers))
        self.Header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
        # print(self.Header)


        if bool(self.env_headers):
            self.Header = self.env_headers

        else:


            if self.cls_name.upper() in ["POST", "PUT", "PATCH"]:
                self.Header.update({
                    'accept': "application/json", "Content-Type": "application/json",

                })

        return ObjectDict(
            {"Header": self.Header,"frontend_env_host":self.frontend_env_host,"backend_env_host":self.backend_env_host,
             "info":self.info,"env_":self.env_}
        )

    @property
    def elapsed(self):
        return Elapsed(self.__request_module)


class Elapsed:

    def __init__(self,e):
        self.e =e

    def total_seconds (self):
        return self.e.elapsed.total_seconds()

    def elapsed(self):
        return self.e.elapsed


    def days (self):
        return self.e.elapsed.days

    def microseconds (self):
        "微秒"
        return self.e.elapsed.microseconds


    def seconds (self):
        """秒"""
        return self.e.elapsed.seconds

    def resolution (self):
        """最小时间"""
        return self.e.elapsed.resolution



class HttpRequestHand(object):
    """用于单独使用的http请求封装API"""

    def __init__(self):

        self.encoding = None

    @request_env()
    def get(self, router: Optional[str],
            data: Optional[Dict]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Sequence[bool]=False,
            env_control:Sequence[bool]=True,
            allow_redirects:Sequence[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """

        if headers is False:
            self.headers_data = self.get.Header
        else:
            self.get.Header.update(headers)


        if router and env_control is True:
            self.__request_module = requests.get(
                url=self._join(router), params=data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects, timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.get(
                url=router, params=data, proxies=proxies, verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self

    @request_env()
    def post(self, router: Optional[str],
            data: Optional[Union[Dict,open]]=None,
            proxies:Optional[Dict]=None,
            # 对SSL证书认证
            verify:Sequence[bool]=False,
            env_control:bool=True,
            allow_redirects:Sequence[bool]=False,
            timeout:Optional[Union[int,float]]=None,
            cookies:Optional[Dict]=None,
            headers:Optional[Union[Dict,bool]]=False,
            # 客户端的证书
            cert:Optional[Union[str,Tuple[str,str]]]=None
            ):
        """

        """


        try:
            _req_data = json.dumps(data) if self.headers_data["Content-Type"] == "application/json" else data

        except:
            _req_data = data

        if router and env_control is True:
            self.__request_module = requests.post(
                url=self._join(router), data=_req_data, proxies=proxies,
                verify=verify, allow_redirects=allow_redirects,
                timeout=timeout, cookies=cookies,cert=cert,
                headers=self.headers_data
            )

        else:
            self.__request_module = requests.post(
                url=router, data=_req_data, proxies=proxies,
                verify=verify,allow_redirects=allow_redirects,timeout=timeout,
                cookies=cookies,headers=self.headers_data,cert=cert,
            )

        return self




    def upload_file(self,file:Optional[Union[List[str],str]],type:Optional[str]="image/png"):
        """
        上传文件
        """
        if isinstance(file,str):
            with open('massive-body', 'rb') as f:
                self.post('http://some.url/streamed', data=f)

        if isinstance(file,list):

            multiple_files = [
                ('images', (x.replace("\\","/").split("/")[-1], open(x, 'rb'), 'image/png'))
                for x in file
            ]
            requests.post('url', files=multiple_files)

        return self

    @request_env()
    def put(self, router: Optional[str],
            data: Optional[Dict]
            ):
        """

        """

        if router:
            self.__request_module = requests.get(url=self._join(router), params=data)

            return self



    def code_ok(self):
        return self.__request_module.codes.ok

    @request_env()
    def delete(self, router: Optional[str],
            data: Optional[Dict]
               ):
        """

        """

        if router:
            self.__request_module = requests.get(url=self._join(router), params=data)

            return self

    @request_env()
    def patch(self, router: Optional[str],
            data: Optional[Dict]):
        """

        """

        if router:
            self.__request_module = requests.patch(url=self._join(router), params=data)

            return self

    @property
    def request_url(self):
        """

        """
        return self.__request_module.request.url

    @property
    def url(self):
        """

        """
        return self.__request_module.url

    @request_env()
    def _join(self, router):
        """

        """
        return '/'.join([self._join.backend_env_host, router])


    @property
    def content(self):
        """

        """
        return self.__request_module.content

    @property
    def text(self):
        """

        """

        return self.__request_module.text

    @property
    def json(self):
        """

        """
        return self.__request_module.json()


    def encoding_(self,coding:Optional[str]="utf-8"):
        """

        """
        self.__request_module.encoding = coding
        return self

    def save_image(self,content:Optional[bytes],fp:Optional[open]):
        """

        """
        from PIL import Image
        from io import BytesIO

        img = Image.open(BytesIO(content))
        img.save(fp=fp)
        return self

    @property
    def request_header(self):
        return HttpRequestHeaders(self.__request_module.request.headers)

    @property
    def request_headers(self):
        return self.__request_module.request.headers


    @property
    def header(self):
        """
        查看请求头
        """
        return HttpResponseHeaders(self.__request_module.headers)

    @property
    def headers(self):
        """
        查看请求头
        """
        return self.__request_module.headers


    @property
    def headers_obj(self):
        """
        查看请求头
        """
        return ObjectDict(self.__request_module.headers)

    @property
    def history(self):
        """
        查看请求头
        """
        return self.__request_module.history

    @property
    def status_code(self):
        """
        查看请求头
        """
        return self.__request_module.status_code

class HttpResponseHeaders:

    def __init__(self,obj:Optional[object]):
        self.obj = obj

    @property
    def content_type(self):
        """"""
        return self.obj["Content-Type"]

    @property
    def connection(self):
        """"""
        return self.obj["Connection"]

    @property
    def content_length(self):
        """"""
        return self.obj["Content-Length"]

    @property
    def keep_alive(self):
        """"""
        return self.obj["Content-Length"]

    @property
    def server(self):
        """"""
        return self.obj["Server"]

    @property
    def permissions_policy(self):
        """"""
        return self.obj["permissions-policy"]

    @property
    def last_modified(self):
        """"""
        return self.obj["Last-Modified"]

    @property
    def access_control_allow_origin(self):
        """"""
        return self.obj["Access-Control-Allow-Origin"]
    @property
    def date(self):
        """"""
        return self.obj["Date"]

    @property
    def strict_transport_security(self):
        """"""
        return self.obj["Strict-Transport-Security"]

    @property
    def etag(self):
        """"""
        return self.obj["ETag"]

    @property
    def expires(self):
        """"""
        return self.obj["expires"]

    @property
    def cache_control(self):
        """"""
        return self.obj["Cache-Control"]

    @property
    def x_proxy_cache(self):
        """"""
        return self.obj["x-proxy-cache"]

    @property
    def accept_encoding(self):
        """"""
        return self.obj["x-proxy-cache"]

class HttpRequestHeaders:

    def __init__(self,obj:Optional[object]):
        self.obj = obj

    @property
    def content_type(self):
        """"""
        return self.obj["Content-Type"]

    @property
    def connection(self):
        """"""
        return self.obj["Connection"]

    @property
    def content_length(self):
        """"""
        return self.obj["Content-Length"]

    @property
    def keep_alive(self):
        """"""
        return self.obj["Content-Length"]

    @property
    def server(self):
        """"""
        return self.obj["Server"]

    @property
    def permissions_policy(self):
        """"""
        return self.obj["permissions-policy"]

    @property
    def last_modified(self):
        """"""
        return self.obj["Last-Modified"]

    @property
    def access_control_allow_origin(self):
        """"""
        return self.obj["Access-Control-Allow-Origin"]
    @property
    def date(self):
        """"""
        return self.obj["Date"]

    @property
    def strict_transport_security(self):
        """"""
        return self.obj["Strict-Transport-Security"]

    @property
    def etag(self):
        """"""
        return self.obj["ETag"]

    @property
    def expires(self):
        """"""
        return self.obj["expires"]

    @property
    def cache_control(self):
        """"""
        return self.obj["Cache-Control"]

    @property
    def x_proxy_cache(self):
        """"""
        return self.obj["x-proxy-cache"]

    @property
    def accept_encoding(self):
        """"""
        return self.obj["x-proxy-cache"]





# https://sveltest-team.github.io/docs/logo.png

if __name__ == '__main__':

    r = RequestBase()

    data= {
    "username":13453001,"password":123456
    }
    # headers = {
    #     "Content-Type": "application/json",
    #     "accept": "application/json",
    #     "X-CSRFToken": "cRw8NvZFJPDzGSPLsie8L9qXH0w0u5ppmwIOg5cmUPREwGP6QGp8rU3E5L27R6hV",
    #     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MzY5NTk1LCJqdGkiOiIwM2FjNjhiNzY4YzU0YWRlOGYyMzYyMTQxN2ZjYzIwMyIsInVzZXJfaWQiOiJkeldmbkhyQWFJRlV5RmJMSENSZiJ9.JwaCHh3zoG69OAZWB1_MiDPKZmKwUGHF7EvdsKY7-WM",
    # }
    # ret = r.put("http://127.0.0.1:8666/api/v1/question/12",data=data,headers=headers,env_control=False).encoding_()
    ret = r.get("https://www.cnblogs.com/rxysg/p/15683537.html",data=json.dumps({"id":111}),env_control=False)
    # data = requests.post("http://127.0.0.1:8666/api/v1/login",headers={"data":'666'},)
    # print(data.json)
    print(r.elapsed.resolution())
    print(r.code_ok())
    # print(data.header.connection)
    # print(data.headers)


    # print(data.status_code == data.code_ok)


