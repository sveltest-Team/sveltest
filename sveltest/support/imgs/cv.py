#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/7
from typing import (Optional, Union,Tuple,List,Dict)

# import cv2
#
# def image_resizer(img_path: Optional[str], save_path: Optional[str], pos: Optional[Union[List, Dict, Tuple]]):
#     """图片裁剪，矩形坐标
#     list or tuple 需要按照x,y坐标来传入如[,y0,y1,x0,x1]
#         left height width top
#     dict 需要按照相关key来
#     int(top):(int(top) + int(height)), int(left):(int(left) + int(width))
#     y:y+h, x:x+w
#
#     """
#     print(pos[-1], (pos[-1] + pos[1]), pos[0], (pos[0] + pos[2]))
#
#     im = cv2.imread(img_path)
#     if isinstance(pos, list) or isinstance(pos, tuple):
#         # im = im[pos[-1]:(pos[-1]+pos[1]), pos[0]:(pos[0]+pos[2])]
#
#         im = im[pos[0]:pos[1], pos[2]:pos[3]]
#         cv2.imwrite(save_path, im)
#
#     if isinstance(pos, dict):
#         print("字典")
