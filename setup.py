
import setuptools  #导入工具包

# with open("requirements.txt") as fin:
#     REQUIRED_PACKAGES = fin.read()
from sveltest.version import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# 读写README.md 文件

setuptools.setup(
    name="sveltest",  #项目名称
    version=version, #项目版本
    author="guanfl", #开发者名称
    author_email="gfl13453001@163.com",  #邮箱
    description="高效率测试开发集成框架",  #描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sveltest-Team/sveltest", #github地址
    packages = setuptools.find_packages(),  # 包含所有src中的包
    # package_dir = {'':'sveltest'},   # 告诉distutils包都在src下

    classifiers=[
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 4 - Beta",
        # 支持的python版本
        # "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], #依赖环境

    # python 依赖版本
    python_requires='>=3.6',

    # Appium-Python-Client==0.49
    # certifi==2019.11.28



    # chardet==3.0.4
    # decorator==4.4.1·
    # facebook-wda==0.4.2
    #
    # Pillow==6.2.1


    # pytesseract==0.3.1
    # python-dateutil==2.8.1
    # requests==2.22.0
    # retry==0.9.2
    # selenium==3.141.0
    # six==1.13.0
    # testdata==1.1.3
    # text-unidecode==1.3
    # urllib3==1.25.7

    install_requires = [
        # 'Appium-Python-Client==0.49',
        'selenium',
        'testdata==1.1.3',
        'PyMySQL==0.9.3',
        'Faker==3.0.0',
        'flanker',
        # 'fastapi==0.65.2',
        # 'uvicorn==0.14.0',
        'requests==2.26.0',
        'rich==10.12.0',
        'yagmail',
        'jinja2',
        # 'gooey==1.0.8.1',
        'pyyaml',
        'NextTestRunner',
        'win10toast',
        'loguru==0.6.0',
        'xmltodict',

    ],#第三方依赖包
    package_data={
            #任何包中含有.txt文件，都包含它
            '': ['*.py','*.py-tpl','*.json','*.html','*.pyc','*.xlsx',"*.*"],
            #包含demo包data文件夹中的 *.dat文件

        },
    keywords = 'sveltest linux python selenium unittest',

    # 命令參數 slt 命令会自动执行指定文件
    entry_points={
            'console_scripts': [
                # 命令 = 包.模块.方法
                'slt=sveltest.bin.conf.base.sveltest_main:main'
            ],
        },

)








