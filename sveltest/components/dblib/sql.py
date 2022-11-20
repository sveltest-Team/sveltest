#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/11/9



# https://blog.csdn.net/wenzhou1219/article/details/83959261
import pymysql
class QueryMetaClass(type):
    def __new__(cls, name, bases, attr_set):
        # print(85,attr_set)

        # 用於存储映射类型属性
        mapping_set = dict()

        # if name == 'QueryDB':
        #     return type.__new__(cls, name, bases, attr_set)


        # print(name)

        # for k, v in attr_dict:
        #     print(k,v)
        #     if isinstance(v, Field):
        #         print("Found Mapping:%s=>%s" % (k, v))
        #         setattr(v, 'name', k)
        #         mapping[k] = v
        #         attr_dict.pop(k)


        for k,v in attr_set.items():
            # print(k)
            # 判断是否是对应的 字段类型
            # if isinstance(v, IntegerField):
                # 将key进行设置成类属性
            setattr(v, "name", k)
            # try:
            #     mapping_set[k] = v
            # except:
            #     pass

            # if isinstance(v,AutoField):
            #     setattr(v, 'char', [k,v._restrain()])
            #     mapping_set[k] = v
                # attr_dict.pop(k)

        # 删除这些已经在字典中存储的属性
        for k in mapping_set.keys():
            attr_set.pop(k)


        # 保存属性和列的映射关系
        # attr_set['__mapping__'] = mapping_set

        # 获取用户定义的表名
        # attr_set['__table__'] = attr_set.get('Meta').table


        return type.__new__(cls, name, bases, attr_set)


class QueryDict:

    def __init__(self,kv,t):
        self.kv = kv
        self.t = t

    def __str__(self):
        try:
            return "<%s:%s>"%(self.t,self.kv["id"])
        except:
            return "<%s:%s>"%(self.t,None)

    def value(self,field):
        return self.kv[field]




class QuerySets:
    def __init__(self,kv,table):
        self.kv = kv
        self.table = table


    def value(self,field):
        return self.kv[field]

    def count(self):
        """统计当前查询的数据总行"""
        pass

    def order_by(self, **kwargs):
        """排序查询"""

    def group_by(self, **kwargs):
        """分组查询"""

    def limit(self, start, end):
        """分页"""

    def cache(self):

        for x in self.kv:
            print(x)

        return

    def __str__(self):
        # <QuerySet [<Article: Na2FdcdrEP>, <Article: skL9jdNijo>, <Article: SqwQpivvjJ>, <Article: Tivlgc2Hei>]>
        xt  = ["<Article: Na2FdcdrEP>"]
        return '<QuerySet [%s]>'


class Cache:
    def __new__(cls, *args, **kwargs):
        return


cache = Cache

class QuerySet(dict):
    def __init__(self, kv,table=None):
        # print(kv)
        self.table = table
        self.kv = kv


        super(QuerySet, self).__init__(kv)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Model has not key %s" % key)

    def __setattr__(self, key, value):
        # if key == "table" or key == "kv":
        #     pass
        # else:
            self[key] = value


    def _getattribute(self,**kwargs):
        self.table = kwargs


    def data_cache(self):
        return


    def filter(self,**kwargs):
        """
        进行过滤筛选
        :param kwargs:
        :return:
        """
        fields = [] # 存放get接收的字段名称
        params = [] # 接收存放get字段的值

        if len(kwargs) > 1:
            print(len(kwargs))

        for k,v in kwargs.items():
            fields.append(k)
            params.append(str(v))

        select_dml = "select * from %s where %s=%s"%(self.table,''.join(fields),''.join(params))
        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)
        # print(_db_info)
        _db_info.execute(select_dml)

        table_fields = _db_info.description
        data = _db_info.fetchone()
        db_ct.commit()
        _db_info.close()


        setattr(cache,"data",data)
        setattr(cache,"field",kwargs)
        setattr(cache,"table",self.table)
        setattr(cache,"type",0)
        if data:
            d = QuerySet(data)
            d.pop("table")
            d.pop("kv")
            return d
        else:
            raise Exception("不存在")
        #
        # data_ = {}
        #
        # _table_fields = [x[0] for x in table_fields]
        # # print(_table_fields)
        #
        # for i,x in enumerate(_table_fields):
        #     try:
        #
        #         data_[x] = data[i]
        #     except:
        #         pass
        #
        # return self.__setattr__(i, x)


    def all(self,**kwargs):
        """获取"""
        fields = [] # 存放get接收的字段名称
        params = [] # 接收存放get字段的值

        for k, v in kwargs.items():
            fields.append(k)
            params.append(str(v))

        select_dml = "select * from %s " % self.table

        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)
        _db_info.execute(select_dml)

        data = _db_info.fetchall()

        db_ct.commit()
        _db_info.close()

        class db:
            def __init__(self,table):
                self.table = table

            def __str__(self):
                return str([QueryDict(x, self.table) for x in data])

            def count(self):
                return len(data)

            @property
            def data(self):
                r = []
                for x in data:
                    x = QuerySet(x, self.table)
                    x.pop("table")
                    r.append(x)

                return r

        return db(self.table)



    def value(self,key):
        """
        获取指定字段的值
        :param key:
        :return:
        """
        cache_ = getattr(cache,"data")
        return cache_[key]

    def delete(self):
        """
        获取指定字段的值
        :param key:
        :return:
        """
        cache_ = getattr(cache,"field")
        table = getattr(cache,"table")
        type = getattr(cache,"type")

        if type == 0:
            filed_ = []
            val = []
            for x in cache_:
                filed_.append(x)
                val.append(str(cache_[x]))

            del_db = "delete from %s where %s=%s"%(table,''.join(filed_),''.join(val))

            db_ct = db_connect().connect_db()
            _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)

            x = _db_info.execute(del_db)
            db_ct.commit()
            _db_info.close()
            db_ct.close()

            return x

    def get(self, **pk):
        """
        用于直接获取一条数据
        :param kwargs: 指定相应的字段与值
        :return:
        """

        fields = [] # 存放get接收的字段名称
        params = [] # 接收存放get字段的值

        for k,v in pk.items():
            fields.append(k)
            params.append(str(v))


        select_dml = "select * from %s where %s=%s"%(self.table,''.join(fields),''.join(params))
        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)

        _db_info.execute(select_dml)

        data = _db_info.fetchone()

        db_ct.commit()
        _db_info.close()

        setattr(cache,"data",data)
        setattr(cache,"field",pk)
        setattr(cache,"table",self.table)
        setattr(cache,"type",0)
        if data:
            d = QuerySet(data)
            d.pop("table")
            d.pop("kv")
            return d
        else:
            raise Exception("不存在")


from sveltest.bin.conf import settings

db_info = getattr(settings,"DATABASE")

class DBConnect(object):
    """
    数据库连接驱动
    """

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.database = "data"
        self.charset = "utf8"
        self.password = "gfl123456"
        self.port = 3306


    def connect_db(self):
        """
        内置的数据库驱动连接
        :return:
        """
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )


class ModelMetaClass(type):
    def __new__(cls, name, bases, attr_set):

        # 用於存储映射类型属性
        mapping_set = dict()

        if name == 'BaseModel':
            return type.__new__(cls, name, bases, attr_set)

        for k, v in attr_set.items():
            # 判断是否是对应的 字段类型
            if isinstance(v, IntegerField):
                # 将key进行设置成类属性
                setattr(v, 'char', [k,v._restrain()])
                mapping_set[k] = v

            if isinstance(v,AutoField):
                setattr(v, 'char', [k,v._restrain()])
                mapping_set[k] = v
                # attr_dict.pop(k)

        # 删除这些已经在字典中存储的属性
        for k in mapping_set.keys():
            attr_set.pop(k)


        # 保存属性和列的映射关系
        attr_set['__mapping__'] = mapping_set

        # 获取用户定义的表名
        attr_set['__table__'] = attr_set.get('Meta').table

        return type.__new__(cls, name, bases, attr_set)



# 为了后续兼容
db_connect = DBConnect

class BaseModel(dict,metaclass=ModelMetaClass,):

    def __init__(self, **kv):

        super(BaseModel, self).__init__(**kv)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Model has not key %s" % key)

    def __setattr__(self, key, value):
        self[key] = value



    def _getattribute(self):
        fields = []
        params = []
        get_fields = []

        for k, v in self.__mapping__.items():
            # print(k, v)
            # 添加对应字段的名称

            fields.append(v.char)
            get_fields.append(k)
            # 获取对应字段的参数并添加到参数列表中
            params.append(getattr(self, k, None))

        return fields,params,get_fields

    def save(self):
        val = self._getattribute()[-2:]
        print(val)

        fields = [str(x) for x in val[-1]]  # 存放get接收的字段名称
        params = [str(x) for x in val[0]]  # 接收存放get字段的值
        # print(params)
        # print(fields,','.join(fields),)

        # values = ''
        # for x in params:
        #     values += f"'{x}',"
        # print()

        # insert_into = "insert into %s (%s) values (%s)"%(self.__table__,','.join(fields),values.strip(","))
        insert_into = "insert into %s (%s) values (%s)"%(self.__table__,','.join(fields),','.join(params))
        print(insert_into)

        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)
        #
        _db_info.execute(insert_into)
        #
        # data = _db_info.fetchone()
        #
        db_ct.commit()
        _db_info.close()
        #
        # setattr(cache, "data", data)
        # setattr(cache, "field", pk)
        # setattr(cache, "table", self.table)
        # setattr(cache, "type", 0)
        # if data:
        #     d = QuerySet(data)
        #     d.pop("table")
        #     d.pop("kv")
        #     return d
        # else:
        #     raise Exception("不存在")
        #
        # print(val)
        # insert_into = f"insert into {self.__table__}  value {self} "
        # try:
        #     _db_info = db_connect().connect_db().execute(insert_into)
        #     if _db_info == 0:
        #         print("创建成功")
        # except:
        #     print("已存在")

    def create_or_update(self):
        pass

    def create_data(self):
        pass


    def drop_database(self):
        """

        :return:
        """
        drop_ddl = f"DROP TABLE {self.__table__}"

        return db_connect().connect_db().execute(drop_ddl)


    @classmethod
    def objects(self):
        """

        :return:
        """
        return QuerySet({},self.__table__)



    def create_db(self):
        """

        :return:
        """
        create_db_ddl = ""
        for i in self._getattribute()[0]:
            create_db_ddl = create_db_ddl + " ".join(i)+","

        rs_ = create_db_ddl.rstrip(",")

        exec_db = "create table %s (%s)"%(self.__table__,rs_)
        # try:
        _db_info = db_connect().connect_db()
        if _db_info == 0:
            print("创建成功")
        # except:
        #     print("已存在")


class Field(object):
    """

    """

    def __init__(self, verbose_name=None, name=None, primary_key=False,
                 max_len=None, unique=False, blank=False, null=False,
                 db_index=False, rel=None,
                 default=None,
                 editable=True,
                 serialize=True, unique_for_date=None, unique_for_month=None,
                 unique_for_year=None, choices=None, help_text='', db_column=None,
                 db_tablespace=None, auto_created=False, validators=(),
                 error_messages=None):
        """

        :param verbose_name:
        :param name:
        :param primary_key:
        :param max_len:
        :param unique:
        :param blank:
        :param null:
        :param db_index:
        :param rel:
        :param default:
        :param editable:
        :param serialize:
        :param unique_for_date:
        :param unique_for_month:
        :param unique_for_year:
        :param choices:
        :param help_text:
        :param db_column:
        :param db_tablespace:
        :param auto_created:
        :param validators:
        :param error_messages:
        """
        self.name = name
        self.verbose_name = verbose_name  # May be set by set_attributes_from_name
        self._verbose_name = verbose_name  # Store original for deconstruction
        self.primary_key = primary_key
        self.max_len, self._unique = max_len, unique
        self.blank, self.null = blank, null
        self.remote_field = rel
        self.is_relation = self.remote_field is not None
        self.default = default
        self.editable = editable
        self.serialize = serialize
        self.unique_for_date = unique_for_date
        self.unique_for_month = unique_for_month
        self.unique_for_year = unique_for_year
        # if isinstance(choices, collections.abc.Iterator):
        #     choices = list(choices)
        self.choices = choices
        self.help_text = help_text
        self.db_index = db_index
        self.db_column = db_column
        self._db_tablespace = db_tablespace
        self.auto_created = auto_created





class FieldChar(Field):


    def name(self):
        return "INT"


    def _check_parm(self):
        """

        :return:
        """


class IntegerField(Field):

    def __init__(self,null=False,default=None,unique=False):
        super(IntegerField, self).__init__(null=null,default=default,unique=unique)
        self.null = null
        self.default= default
        self.unique = unique

        # if min_value is not None:
        #     if not isinstance(min_value, numbers.Integral):
        #         raise ValueError("min_value must be int")
        #     elif min_value < 0:
        #         raise ValueError("min_value must be positive int")
        # if max_value is not None:
        #     if not isinstance(max_value, numbers.Integral):
        #         raise ValueError("max_value must be int")
        #     elif max_value < 0:
        #         raise ValueError("max_value must be positive int")
        # if min_value is not None and max_value is not None:
        #     if min_value > max_value:
        #         raise ValueError("min_value must be smaller than max_value")
        #


        self._restrain()

    # def __get__(self, instance, owner):
    #     return self._value

    # def __set__(self, instance, value):
    #     if not isinstance(value, numbers.Integral):
    #         raise ValueError("int value need")
    #     if value < self.min_value or value > self.max_value:
    #         raise ValueError("value must between min_value and max_value")
    #     self._value = value



    def _restrain(self):
        # print(self.null)
        if self.default:
            NULL = arg.DB_ARGUMENT["DEFAULT_NULL"] if self.null else f"NOT NULL DEFAULT '{self.default}'"

        elif self.unique:
            NULL = arg.DB_ARGUMENT["DEFAULT_NULL"] if self.null else f"NOT NULL  UNIQUE"
        else:

            NULL = arg.DB_ARGUMENT["DEFAULT_NULL"] if self.null else arg.DB_ARGUMENT["NOT_NULL"]
        return F"INT(10) {NULL}"

# 枚举

class Argument:

    DB_ARGUMENT = {
        "DEFAULT_NULL":"DEFAULT NULL",
        "NOT_NULL":"NOT NULL"
    }

arg = Argument

class AutoField(Field):

    def __init__(self,primary_key=True):
        super(AutoField, self).__init__(primary_key=primary_key)
        self._restrain()

    def _restrain(self):
        return "INT(10)  NOT NULL AUTO_INCREMENT PRIMARY KEY"

class CharField(Field):

    def __init__(self,null=False,max_len=10,default=None,unique=False):
        super(CharField, self).__init__(null=null,max_len=max_len,default=default,unique=unique)
        self._restrain()

    def _restrain(self):
        return f"varchar({self.max_len})  NOT NULL AUTO_INCREMENT PRIMARY KEY"


class UserModel(BaseModel):
    id = AutoField()
    name = CharField(default=1)
    age = IntegerField(unique=True)

    class Meta:
        table = "userdata"


if __name__ == '__main__':
    x = UserModel(id=3,name="中",age="4")
    x.create_db()

    print(x)

# INT 整型

# def name(self):
#     return 12
#
# Test2 = type("Test2",(UserModel,), {"name":name}) # 定了一个Test2类
# x = Test2()
# print(x.name())
# https://www.runoob.com/mysql/mysql-data-types.html


# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='testuser',
#                      password='test123',
#                      database='TESTDB')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()
#

