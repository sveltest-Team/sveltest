#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/10/9


 # b"bin/tools/pdfImg.exe"
PDFIMGPATH = b'YmluL3Rvb2xzL3BkZkltZy5leGU='
# '{base_path} -r {idp} -png "{pdf_file}" "{img_path}\{file_prefix}"'
PDFIMGPATH_SHELL = b'e2Jhc2VfcGF0aH0gLXIge2lkcH0gLXBuZyAie3BkZl9maWxlfSIgIntpbWdfcGF0aH1ce2ZpbGVfcHJlZml4fSI='

# '{base_path} -f {start_page} -l {end_page} -r {idp} -png "{pdf_file}" "{img_path}\{file_prefix}"'
PDFIMG_RANGE = b'e2Jhc2VfcGF0aH0gLWYge3N0YXJ0X3BhZ2V9IC1sIHtlbmRfcGFnZX0gLXIge2lkcH0gLXBuZyAie3BkZl9maWxlfSIgIntpbWdfcGF0aH1ce2ZpbGVfcHJlZml4fSI='


if __name__ == '__main__':

    import base64


    # x = bytes(PDFIMGPATH, encoding="utf-8")
    x = PDFIMG_RANGE
    m = base64.b64encode(x)
    print(m)
    print(
        base64.b64decode(PDFIMG_RANGE).decode().format(base_path="adb", pdf_file="ssefc", img_path=1, file_prefix=1)
    )
