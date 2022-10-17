#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/6/9
import json

import uvicorn
from fastapi import FastAPI



app = FastAPI(title="sweet 接口demo服务 ",
              description="""""",
              version="1.1")



# 请求根目录
@app.get('/')
def index():
    return {'code':0,'message': '欢迎使用 sveltest 框架 ,接口测试demo服务！'}

def get_cityids():
    data = json.load(open("cityids.json","r",encoding="utf-8"))
    data_json = {}
    for x in data:
        areaid = x["areaid"]
        countyname = x["countyname"]
        data_json[countyname] = areaid
    return data_json


def requests_weather(city_id):
    import requests
    url = f"http://aider.meizu.com/app/weather/listWeather?cityIds={city_id}"
    data = requests.get(url=url)
    dc_data = json.loads(data.content.decode("utf-8"))
    # 当前查询的城市名称
    current_city_name = dc_data["value"][0]["city"]
    # 查询的城市的省名
    current_province_name = dc_data["value"][0]["provinceName"]
    # 当前实时查询数据
    current_realtime = dc_data["value"][0]["realtime"]
    [current_realtime.pop(x) for x in ["sD","ziwaixian","img"]]
    # 城市未来六天的天气情况
    weathers = dc_data["value"][0]["weathers"]
    for i in range(len(weathers)):
        for x in ["sun_down_time", "sun_rise_time", "img", "temp_day_f", "temp_night_f","wd","ws"]:
            weathers[i].pop(x)
    # 当天的具体指标
    indexes = dc_data["value"][0]["indexes"]
    # 空气质量
    kq = dc_data["value"][0]["pm25"]
    [kq.pop(x) for x in ["advice", "citycount", "cityrank","co","color","level","no2","o3","pm10","pm25","so2","timestamp","upDateTime"]]
    data = {
        "city_id":city_id,"city_name":current_city_name,"province_name":current_province_name,
        "current_realtime":current_realtime,"weathers":weathers,"indexes":indexes,"kq":kq
    }
    return data
# 请求根目录
@app.get(
    '/weather/{cityname}',
    tags=["查询天气"],
    description="根据城市的名称进行查询当前城市的天气",
    summary="查询天气"
)
def index(cityname:str):
    """查询"""
    if cityname:
        try:
            city_id = get_cityids()[cityname]
            return requests_weather(city_id=city_id)
        except:
            return {'code':-1,'message': '没有查询到相对应的城市'}
    else:
        return {'code':1,'message': '请输入需要查询的城市名称'}


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=6688)
