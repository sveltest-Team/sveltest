#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/10/21
import importlib




class ImportString:
    """
    使用字符串进行动态导入模块
    """
    def import_string(self,dotted_path):
        """
        Import a dotted module path and return the attribute/class designated by the
        last name in the path. Raise ImportError if the import failed.
        """
        try:
            module_path, class_name = dotted_path.rsplit('.', 1)

        except ValueError as err:
            raise ImportError("%s doesn't look like a module path" % dotted_path) from err



        module = importlib.import_module(module_path)


        try:
            return getattr(module, class_name)
        except AttributeError as err:
            raise ImportError('Module "%s" does not define a "%s" attribute/class' % (
                module_path, class_name)
                              ) from err


importString = ImportString()





