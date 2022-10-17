#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""

                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|


"""
import base64
import io
import os
import re
import shutil
import sys
import zipfile

from typing import Optional,List

# v 1.0
# guanfl
# 2021.5.28
# :TODO 已完成 待单元测试
from sveltest.bin.conf.license import PDFIMGPATH, PDFIMGPATH_SHELL, PDFIMG_RANGE


class StFile:
    def __init__(self):
        pass


    def get_path_list(self,path:Optional[str]) -> List:
        """
        指定目录下的所有文件路径
        :param path:
        :return:
        """

        assert os.path.isdir(path), '%s not exist.' % path
        ret = []
        for root, dirs, files in os.walk(path):
            for filespath in files:
                ret.append(os.path.join(root, filespath))
        return ret

    def copy_all(self,src_path:Optional[str], target_path:Optional[str]) -> Optional[bool]:
        """

        :param src_path:
        :param target_path:
        :return:
        """

        if os.path.isdir(src_path) and os.path.isdir(target_path):
            filelist_src = os.listdir(src_path)
            for file in filelist_src:
                path = os.path.join(os.path.abspath(src_path), file)
                if os.path.isdir(path):
                    path1 = os.path.join(os.path.abspath(target_path), file)
                    if not os.path.exists(path1):
                        os.mkdir(path1)
                    self.copy_all(path, path1)
                else:
                    with open(path, 'rb') as read_stream:
                        contents = read_stream.read()
                        path1 = os.path.join(target_path, file)
                        with open(path1, 'wb') as write_stream:
                            write_stream.write(contents)
            return True
        else:
            return False

    def dir_copy(self,src_path:Optional[str], target_path:Optional[str]):
        """copy
        all
        files
        of
        src_path
        to
        target_path"""
        # 将某文件夹下所有文件复制至指定文件夹内，但不复制该文件夹的结构
        file_count = 0
        source_path = os.path.abspath(src_path)
        target_path = os.path.abspath(target_path)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        if os.path.exists(source_path):
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    src_file = os.path.join(root, file)
                    shutil.copy(src_file, target_path)
                    file_count += 1
                    print(src_file)
        return int(file_count)

    def isdir(self,path:Optional[str]):
        """

        :param path:
        :return:
        """
        p = os.path.splitext(path)
        if p[1]:
            return False
        else:
            return True

    def isfile(self,path:Optional[str]):
        """

        :param path:
        :return:
        """
        p = os.path.splitext(path)
        if p[-1]:
            if not os.listdir(path):
                return False
            else:
                return True
        else:
            return False


    def is_listdir(self,path:Optional[str]):
        """

        :param path:
        :return:
        """
        file_list = os.listdir(path)
        file = []
        dir = []
        other_files = []
        listfile = {
            "file": file,
            "dir": dir,
            "other_files": other_files
        }
        for i in file_list:
            p = os.path.splitext(i)
            if p[-1]:
                if p[-1] == ".zip" or p[-1] == ".rar":
                    other_files.append(i)
                    print("{} 目录下 {} 压缩文件".format(path, i))
                else:
                    file.append(i)
                    print("{} 目录下 {} 是文件".format(path, i))
            else:
                dir.append(i)
                print("{} 目录下 {} 是文件夹".format(path, i))
        return listfile

    def del_type_file(self,path:Optional[str], filename:Optional[str]):
        """

        :param path:
        :param filename:
        :return:
        """
        pathfile = os.listdir(path)
        for files in pathfile:
            join_file_path = os.path.join(path, files)
            where = os.path.splitext(files)

            if where[-1] == filename:

                os.remove(join_file_path)
                print("已删除{}".format(files))



    def del_all_file(self,path):
        """

        :param path:
        :return:
        """
        pathfile = os.listdir(path)
        for files in pathfile:
            join_file_path = os.path.join(path, files)
            if os.path.isfile(join_file_path):
                os.remove(join_file_path)
                print("已删除{}".format(files))
            else:
                try:
                    self.del_all_file(join_file_path)
                    os.rmdir(join_file_path)
                    print("已删除{}".format(files))
                except:
                    self.del_all_file(join_file_path)
                print("已删除{}".format(files))

    def del_current_file(self,path):
        """

        :param path:
        :return:
        """
        pathfile = os.listdir(path)
        for files in pathfile:
            join_file_path = os.path.join(path, files)
            if os.path.isfile(join_file_path) == True:
                os.remove(join_file_path)
                print("已删除{}".format(files))





class ZipFile:
    """"""
    def __init__(self):
        self.pathFile = None
        self._filer = []

    def all_path(self, path):
        """

        :param path:
        :return:
        """
        # 递归获取目录下所有文件
        join = os.listdir(path)

        for d in join:
            die = os.path.join(path, d)
            try:
                self.all_path(die)
                self._filer.append(die)
            except:
                self._filer.append(die)
        return self._filer

    def zip_file(self,path, zipfile_name):
        """
        Args:
            path:传入一个需要压缩的文件夹路径
            zipfile_name:压缩包的存放路径
        return:
            传出的是一个压缩包的存放路径
        """
        # 压缩zip文件 path压缩的文件夹路径 压缩文件路径+.zip
        path = path
        join = os.listdir(path)
        join_path = []

        for i in join:
            public = os.path.join(path, i)
            join_path.append(public)

        f = zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED)

        for s in join_path:
            jie = s.replace("\\", "/").split('/')
            index = jie[-1]
            f.write(s.replace("\\", "/"), index)

        f.close()

        return zipfile_name

    def all_zip(self, zipfile_name, path):
        """
        打包所有
        :param zipfile_name:
        :param path:
        :return:
        """
        _path = self.all_path(path)
        f = zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED)
        for adb in _path:
            f.write(adb)

        f.close()
        return _path


    def extract(self,filename):
        """
        进行解压
        :param filename:
        :return:
        """
        z = zipfile.ZipFile(filename)
        for f in z.namelist():
            # get directory name from file
            dirname = os.path.splitext(f)[0]
            # create new directory
            os.mkdir(dirname)
            # read inner zip file into bytes buffer
            content = io.BytesIO(z.read(f))
            zip_file = zipfile.ZipFile(content)
            for i in zip_file.namelist():
                zip_file.extract(i, dirname)

# 是否包含中文字符
def is_chinese(string:Optional[str]) -> bool:
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


class FileHandle:
    """
    文件操作
    """


    def link(self,path,oj):
        """
         用于创建硬连接的源地址
         用于创建硬连接的目标地址
        :param path:
        :param oj:
        :return:
        """
        try:
            os.link(path,oj)
            return 0
        except:
            return 1

    def isfile(self,file):
        """
        是否存在该文件
        :return:
        """
        return os.path.exists(file)



# v1.2.2
# 20210723
from PIL import Image

import subprocess


class LicenseBaseDecode:
    """

    """
    PDFIMG_EXE_PATH = base64.b64decode(PDFIMGPATH).decode()
    # print(PDFIMG_EXE_PATH)



code = LicenseBaseDecode


class ToolsBase:
    BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

    PDFIMG = os.path.join(BASE_DIR, code.PDFIMG_EXE_PATH).replace('\\', '/')

    PDFIMG_SHELL = base64.b64decode(PDFIMGPATH_SHELL).decode()
    PDFIMG_RANGE_IMG = base64.b64decode(PDFIMG_RANGE).decode()



base_commandline = ToolsBase
class PDFObject:

    def __init__(self,path=None):
        """
          -f <int>                 : 要转换的前面第几页
          -l <int>                 : 要转换的最后一页
          -o                       : 只打印奇数页
          -e                       : 只打印偶数页
          -singlefile              : 只写第一页，不要加数字
          -r <fp>                  : resolution, in DPI (default is 150) 分辨率
          -rx <fp>                 : X分辨率，DPI(默认为150)
          -ry <fp>                 : Y resolution, in DPI (default is 150)
          -scale-to <int>          : 缩放每一页以适应从比例到*比例到像素的框
          -scale-to-x <int>        : scales each page horizontally to fit in scale-to-x pixels
          -scale-to-y <int>        : scales each page vertically to fit in scale-to-y pixels
          -x <int>                 : x-coordinate of the crop area top left corner
          -y <int>                 : y-coordinate of the crop area top left corner
          -W <int>                 : 裁剪区域的宽度(以像素为单位)(默认为0)
          -H <int>                 : height of crop area in pixels (default is 0)
          -sz <int>                : 裁剪正方形的大小(以像素为单位)(集合W和H)
          -cropbox                 : 使用裁剪框而不是媒体框
          -mono                    : generate a monochrome PBM file
          -gray                    : generate a grayscale PGM file
          -png                     : generate a PNG file
          -jpeg                    : generate a JPEG file
          -jpegopt <string>        : jpeg options, with format <opt1>=<val1>[,<optN>=<valN>]*
          -tiff                    : generate a TIFF file
          -tiffcompression <string>: set TIFF compression: none, packbits, jpeg, lzw, deflate
          -freetype <string>       : enable FreeType font rasterizer: yes, no
          -thinlinemode <string>   : set thin line mode: none, solid, shape. Default: none
          -aa <string>             : enable font anti-aliasing: yes, no
          -aaVector <string>       : enable vector anti-aliasing: yes, no
          -opw <string>            : owner password (for encrypted files)
          -upw <string>            : user password (for encrypted files)
          -q                       : don't print any messages or errors
          -v                       : print copyright and version info
          -h                       : print usage information
          -help                    : print usage information
          --help                   : print usage information
          -?                       : print usage information
        """
        self.path = path
        # 获取当前文件的父级目录名称




    def _rea(self,path, pdf_name):
        """
        目前仅支持 jpg、png、jpeg格式图片
        :param path:
        :param pdf_name:
        :return:
        """
        file_list = os.listdir(path)
        pic_name = []
        im_list = []
        for x in file_list:
            if "jpg" in x or 'png' in x or 'jpeg' in x:
                pic_name.append(x)

            pic_name.sort()
            new_pic = []

            for x in pic_name:
                if "jpg" in x:
                    new_pic.append(x)

            for x in pic_name:
                if "png" in x:
                    new_pic.append(x)


            im1 = Image.open(os.path.join(path, new_pic[0]))

            new_pic.pop(0)
        for i in new_pic:

            img = Image.open(os.path.join(path, i))
            if img.mode == "RGBA":
                img = img.convert('RGB')

                im_list.append(img)
            else:
                im_list.append(img)

        im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)

    def save(self,filepath):
        """

        """
        if ".pdf" in filepath:
            self._rea(self.path, pdf_name=filepath)
            print("pdf已生成完成")
        else:
            self._rea(self.path, pdf_name="{}.pdf".format(filepath))
            print("pdf已生成完成")


    def png(self, pdf_file:Optional[str], img_path:Optional[str],
            file_prefix:Optional[str]="sveltest",dpi=150,
            range_out:Optional[List]=None
            ) -> Optional[object]:
        """

        """

        if is_chinese(img_path):
            raise Exception("图片输出的路径不能包含中文")

        if range_out:
            self._range_png(pdf_file=pdf_file,img_path=img_path,file_prefix=file_prefix,dpi=dpi,
                            first_page=range_out[0],last_page=range_out[-1])

        return subprocess.Popen(
            base_commandline.PDFIMG_SHELL.format(
                base_path=base_commandline.PDFIMG, pdf_file=pdf_file, img_path=img_path,
                file_prefix=file_prefix,idp=dpi
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        ).communicate()[0]

    def _range_png(self, pdf_file:Optional[str], img_path:Optional[str],
            file_prefix:Optional[str]="sveltest",dpi=150,
            first_page=None,last_page=None,
            ) -> Optional[object]:


        return subprocess.Popen(
            base_commandline.PDFIMG_RANGE_IMG.format(
                base_path=base_commandline.PDFIMG, pdf_file=pdf_file, img_path=img_path,
                file_prefix=file_prefix,idp=dpi,start_page=1,end_page=1
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        ).communicate()[0]






    def jpeg(self, pdf_file, path):
        """

        """
        subprocess.Popen('"%s" -jpeg "%s" "%s"\image' % (self.PDFTOPPMPATH, pdf_file, path)).communicate()[0]



class TXTObject:

    def __init__(self):
        """
        """
        # 获取当前文件的父级目录名称
        self.BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        self.PDFTOTEXT = os.path.join(self.BASE_DIR, 'default/conf/poppler/bin/pdftotext.exe').replace('\\', '/')

    def txt(self,pdf_file,path,filename=None):
        """
        用法：pdftotext [options] <PDF-file> [<text-file>]
          -f <int> : 要转换的第一页
          -l <int> : 要转换的最后一页
          -r <fp> : 分辨率，以 DPI 为单位（默认为 72）
          -x <int> : 裁剪区域左上角的 x 坐标
          -y <int> : 裁剪区域左上角的 y 坐标
          -W <int> ：以像素为单位的裁剪区域宽度（默认为 0）
          -H <int> : 裁剪区域的高度（以像素为单位）（默认为 0）
          -layout : 保持原来的物理布局
          -fixed <fp> ：假设固定间距（或表格）文本
          -raw ：按内容流顺序保留字符串
          -htmlmeta : 生成一个简单的 HTML 文件，包括元信息
          -enc <string> : 输出文本编码名称
          -listenc : 列出可用的编码
          -eol <string> : 输出行尾约定（unix、dos 或 mac）
          -nopgbrk : 不要在页面之间插入分页符
          -bbox ：将每个单词和页面大小的边界框输出到 html。设置 -htmlmeta
          -bbox-layout ：类似于 -bbox 但具有额外的布局边界框数据。设置 -htmlmeta
          -opw <string> ：所有者密码（用于加密文件）
          -upw <string> : 用户密码（用于加密文件）
          -q : 不打印任何消息或错误
          -v : 打印版权和版本信息
          -h : 打印使用信息
          -help : 打印使用信息
          --help : 打印使用信息
          -？: 打印使用信息
        :param pdf_file:
        :param path:
        :return:
        """


        # -raw 保留字符顺序流
        # layout 按照布局进行输出文本内容
        # htmlmeta 生成简单的html

        p = subprocess.Popen('"%s" -htmlmeta1 "%s" "%s"\math_hw.txt' % (self.PDFTOTEXT, pdf_file, path)).communicate()[0]


class ReNumber:
    def __init__(self):
        self.val = None

    def number(self,str):
        """匹配数字"""
        pattern = re.compile(r'^[0-9]*$')
        if pattern.findall(str):
            self.val = pattern.findall(str)
            return  True
        else:
            return False

    def numbers(self,str,n):
        """n 位数"""
        pattern = re.compile(r'^\d{%s}$'%n)
        if pattern.findall(str):
            self.val = pattern.findall(str)
            return True
        else:
            return False

    def least_number(self,str,n):
        """至少多少位数字"""
        pattern = re.compile(r'^\d{%s,}$'%n)
        if pattern.findall(str):
            self.val = pattern.findall(str)
            return True
        else:
            return False


    def border_number(self,str,min,max):
        """边界值min、max"""
        pattern = re.compile(r'^\d{%s,%s}$'%(min,max))
        if pattern.findall(str):
            self.val = pattern.findall(str)
            return True
        else:
            return False
