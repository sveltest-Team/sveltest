#!/usr/bin/env python
# -*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/14
import os
from pathlib import Path
from typing import (Optional, Dict, Tuple, List)

from sveltest import RequestBase
from sveltest.support.common import ObjectDict

from sveltest.components.jinja_template import JinJaTemplate
import json


# os.path.join(Path(__file__).resolve().parent,"bin\conf\html")
class AnalysisPost(RequestBase):
    """

    """

    def __init__(self, json_file=Optional[open], temp_file: str = "template.py-tpl", export_path: str = None):
        """"
        """
        super(AnalysisPost, self).__init__()

        self.json_file_path = json_file
        self.temp = temp_file
        self.path = export_path
        self.temp_jinja = JinJaTemplate(
            temp_dir=os.path.join(Path(__file__).resolve().parent.parent, "_postmanExportjsonAnalysis"))

    def _read_json(self):
        """

        """
        return json.load(fp=open(self.json_file_path, encoding="utf-8"), )

    def _read_temp(self, tempfile: Optional[str]):
        """

        """
        # print(self._read_json())
        # print(os.path.join(Path(__file__).resolve().parent.parent,"_postmanExportjsonAnalysis"))

        return self.temp_jinja.get_template(t=tempfile)

    def _http(self, method, path, headers, data):
        """

        """
        if str(method).upper() == "GET":
            return self._read_temp(tempfile="method_get.py-tpl").render(
                path=path, headers=headers if headers else {}, data=data if data else {})
        elif str(method).upper() == "POST":
            return self._read_temp(tempfile="method_post.py-tpl").render(
                path=path, headers=headers if headers else {}, data=data if data else {})
        elif str(method).upper() == "PUT":
            return self._read_temp(tempfile="method_put.py-tpl").render(
                path=path, headers=headers if headers else {}, data=data if data else {})

    def parse(self):
        """

        """
        data = ObjectDict(self._read_json())
        _variable = data.variable
        _info = data.info
        # _item = data.item
        _item = data.item

        content_method = ""
        for i, xl in enumerate(_item):
            obj = ObjectDict(xl)
            _item_name = obj.name
            _item_sub_item = obj.item
            if _item_sub_item:
                print(_item_sub_item)
            else:
                _item_request = ObjectDict(obj.request)
                _item_response = obj.response
                _item_request_method = _item_request.method
                _item_request_header = _item_request.header

                # 处理header
                _header_data = {}
                if isinstance(_item_request_header,list):

                    for head in _item_request_header:
                        _head = ObjectDict(head)
                        if _head.disabled:

                            continue
                        else:
                            _header_data[_head.key] = _head.value


                # 处理body
                body_data = {}
                try:
                    _item_request_body = ObjectDict(_item_request.body)
                    mode_ = _item_request_body.mode

                    if mode_ in ["formdata"]:
                        # print(_item_request_body[mode_])
                        for by in _item_request_body[mode_]:
                            body_ = ObjectDict(by)
                            if body_.disabled:
                                continue
                            else:
                                body_data[body_.key] = body_.value
                except:
                    _item_request_body = None


                _item_request_url = ObjectDict(_item_request.url)

                # 处理query
                query_data = {}
                if _item_request_url:
                    protocol = _item_request_url.protocol
                    path = _item_request_url.path
                    query = _item_request_url.query

                    if query:
                        for x in query:
                            _x = ObjectDict(x)
                            if _x.disabled:

                                continue
                            else:
                                query_data[_x.key] = _x.value


                if not body_data :
                    content_method = content_method + self._read_temp(tempfile="method_.py-tpl") \
                        .render(def_doc=_item_name, case_code=self._http(method=_item_request_method,
                                                                         path=_item_request_url.raw,
                                                                         headers=_header_data, data=body_data),
                                methods_name=i)

                elif not query_data:
                    content_method = content_method + self._read_temp(tempfile="method_.py-tpl") \
                        .render(def_doc=_item_name, case_code=self._http(method=_item_request_method,
                                                                         path=_item_request_url.raw,
                                                                         headers=_header_data, data=query_data),
                                methods_name=i)
                else:
                    content_method = content_method + self._read_temp(tempfile="method_.py-tpl") \
                        .render(def_doc=_item_name, case_code=self._http(method=_item_request_method,
                                                                         path=_item_request_url.raw,
                                                                         headers=_header_data, data=None),
                                methods_name=i)


        script_content = self._read_temp(tempfile="template.py-tpl").render(
            class_name="TestExportCase", setup_code="pass", tearDown="pass", testcase_code=content_method
        )

        with open(self.path, "a", encoding="utf-8") as f:
            f.write(script_content)



if __name__ == '__main__':
    # file_path = r"F:\demo\sveltest\sveltest\bin\conf\base\_postmanExportjsonAnalysis\template.py-tpl"
    an = AnalysisPost(
        json_file=r"F:\demo\sveltest\sveltest\bin\conf\base\_postmanExportjsonAnalysis\浏览器.postman_collection.json", )
    an.parse()

    # print(an)
