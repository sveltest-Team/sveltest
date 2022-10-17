#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/8/29


"""
                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|
"""


from faker import Faker

from sveltest.support import LanguageException


class VirtualData:
    def __init__(self,language="zh_CN"):
        # 简体中文：zh_CN
        # 繁体中文：zh_TW
        # 美国英文：en_US
        # 英国英文：en_GB
        # 德文：de_DE
        # 日文：ja_JP
        # 韩文：ko_KR
        # 法文：fr_FR

        if language in [
            "zh_CN","zh_TW","en_US","en_GB","de_DE",
            "ja_JP","ko_KR","fr_FR"
        ]:
            self.get_data = Faker(locale=language)
        else:
            raise LanguageException(msg="不支持的语言类型")



    def country(self,mode=None):
        """

        :param mode: suffix 省市县级 code 国家编码

        :return:
        """
        # 国家
        if mode is None:
            return self.get_data.country()
        elif mode == "suffix":
            return self.city_suffix()
        elif mode == "code":
            return self.get_data.country_code()


    def city_suffix(self):
        """城市的末尾标识"""
        # self.get_data.seed(100)
        return self.get_data.city_suffix()

    def address(self,count=None):
        """地址"""
        if count is None:

            return self.get_data.address()
        else:
            return [self.get_data.address() for x in range(count)]


    def alphabet(self,isupper=False):
        """生成英文字母
        """
        txt = ''
        if isupper is False:
            txt = self.get_data.random_element()
        else:
            while True:
                d = self.get_data.random_letter()
                if d.isupper():
                    txt = d
                    break

        return  txt

    def date(self):
        return self.get_data.date()

    def country_code(self):
        return self.get_data.date()


    def opera_user_agent(self):
        """随机生成Opera的浏览器user_agent信息"""
        return self.get_data.opera()

    def safari_user_agent(self):
        """随机生成Safari的浏览器user_agent信息"""
        return self.get_data.safari()

    def chrome_user_agent(self):
        """随机生成chrome的浏览器user_agent信息"""
        return self.get_data.chrome()

    def firefox_user_agent(self):
        """随机生成firefox的浏览器user_agent信息"""
        return self.get_data.firefox()

    def internet_exploreruser_agent(self):
        """随机生成ie的浏览器user_agent信息"""
        return self.get_data.internet_explorer()

    def linux_platform_token(self):
        """随机Linux信息"""
        return self.get_data.linux_platform_token()

    def user_agent(self):
        """随机user_agent信息"""
        return self.get_data.user_agent()





# ● fake.city_suffix()：市，县
# ● fake.country()：国家
# ● fake.country_code()：国家编码
# ● fake.district()：区
# ● fake.geo_coordinate()：地理坐标
# ● fake.latitude()：地理坐标(纬度)
# ● fake.longitude()：地理坐标(经度)
# ● fake.postcode()：邮编
# ● fake.province()：省份
# ● fake.address()：详细地址
# ● fake.street_address()：街道地址
# ● fake.street_name()：街道名
# ● fake.street_suffix()：街、路

if __name__ == '__main__':
    x = VirtualData()
    print(x.opera_user_agent())
