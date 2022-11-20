#!/usr/bin/env python
#-*- coding:utf-8 -*-



# 枚举数据库相关所有字段类型及约束

#自增(int)


AUTO_INCREMENT = "AUTO_INCREMENT" # AUTO_CREMENT
# 不为空
NOT_NULL = "NOT NULL"
# 为空
NULL = "NULL"
# 默认值
DEFAULT = "DEFAULT"
# 字段说明
COMMENT  = "COMMENT {{name}}"

# 字段
Field_SQL = {
    'Integer': ("{{field_name}} integer{% if max_len  %}({{max_len}}){% endif %} {% if null  %}NULL{%elif null==false%} NOT NULL {% endif %}"
             "{% if primary_key %} PRIMARY KEY  {% endif %} {% if auto_increment %}AUTO_INCREMENT {% endif %} {% if unique %} UNIQUE  {% endif %}"
             "{% if default==true or default==0 %}DEFAULT {% if default is number %}{{default}} {% else %} '{{default}}'{% endif %} {% endif %} {% if verbose_name %}COMMENT '{{verbose_name}}'  {% endif %}"),
    'Varchar':( "{{field_name}} varchar{% if max_len  %}({{max_len}}){% endif %} {% if null  %}NULL{%elif null==false%} NOT NULL  {% endif %} "
             "{% if primary_key %} PRIMARY KEY  {% endif %} {% if auto_increment %}AUTO_INCREMENT {% endif %} {% if unique %} UNIQUE  {% endif %} "
             "{% if default==true or default==0 %}DEFAULT {% if default is number %}{{default}}{% else %}'{{default}}'{% endif %} {% endif %} {% if verbose_name %}COMMENT '{{verbose_name}}'  {% endif %}"),
    'Bigint': (
        "{{field_name}} bigint{% if max_len  %}({{max_len}}){% endif %} {% if null  %}NULL{%elif null==false%} NOT NULL  {% endif %} "
        "{% if primary_key %} PRIMARY KEY  {% endif %} {% if auto_increment %}AUTO_INCREMENT {% endif %} {% if unique %} UNIQUE  {% endif %} "
        "{% if default==true or default==0 %}DEFAULT {% if default is number %}{{default}}{% else %}'{{default}}'{% endif %} {% endif %} {% if verbose_name %}COMMENT '{{verbose_name}}'  {% endif %}"),
    'default': (
        "{{field_name}} {{type}}{% if max_len  %}({{max_len}}){% endif %} {% if null  %}NULL{%elif null==false%} NOT NULL  {% endif %} "
        "{% if primary_key %} PRIMARY KEY  {% endif %} {% if auto_increment %}AUTO_INCREMENT {% endif %} {% if unique %} UNIQUE  {% endif %} "
        "{% if default==true or default==0 %}DEFAULT {% if default is number %}{{default}}{% else %}'{{default}}'{% endif %} {% endif %} {% if verbose_name %}COMMENT '{{verbose_name}}'  {% endif %}"),

}

SQL_DDL = {
    "CREATE":("create table {{table_name}} ({{table_field}}) {% if comment %} COMMENT='{{comment}}'  {% endif %}"),
    "INSERT_VAL":("insert into {{table_name}} set {% for k,item in insert_val.items() %}{{k}}={{ item }},{% endfor %}"),
    "DROP":("DROP TABLE {{table_name}}"),
    "DROP_EXISTS":("DROP TABLE IF EXISTS {{table_name}}"),
    "DELETE":("DELETE FROM {{table_name}} {{_WHERE}} {{_ORDER_BY}}"),
    "DELETE_JOIN":("{{SQL_MAIN}} {% if _WHERE %}{{_WHERE}}{% endif %}{% if _ORDER_BY %}{{_ORDER_BY}}{% endif %}{% if _GROUP_BY %}{{_GROUP_BY}} {% endif %}"
                   "{% if _HAVING %}{{_HAVING}} {% endif %}"),
    "SELECT":("SELECT * FROM {{table_name}} {{_WHERE}} {{_ORDER_BY}} {{_GROUP_BY}}"),
    "UPDATE":("UPDATE {{table_name}} SET {% for k,item in update_val.items() %}{% if loop.last %}{{k}}={{item}}{%else%}{{k}}={{item}},{% endif %}"
              "{% endfor %} {{_WHERE}} {{_ORDER_BY}}"
              "{{LIMIT}}"),
    # "DELETE":("DELETE FROM {{table_name}} {% if filter %} WHERE {{expression}}  {% endif %} {% if order_by %} ORDER BY {{expression}}  {% endif %}"
    #           "{% if limit %} LIMIT {{expression}}  {% endif %}"),
    "_WHERE":("{% if filter %}WHERE {{expression}}  {% endif %}"),
    "_ORDER_BY":("{% if order_by %}ORDER BY {{expression}}  {% endif %}"),
    "_GROUP_BY":("{% if group_by %}GROUP BY {{expression}}  {% endif %}"),
    "_HAVING":("{% if having %}HAVING {{expression}}  {% endif %}"),
    "DELETE_LIMIT":("{% if limit %} LIMIT {{expression}}  {% endif %}"),
    "TRUNCATE":("TRUNCATE TABLE {{table_name}}"),
    "DISTINCT":("SELECT DISTINCT {% if table_field %} {{table_field}} {%else%} * {% endif %} FROM {{table_name}}"),
}




if __name__ == '__main__':
    from sveltest.components.jinja_template import StringTemplate
    jk = StringTemplate(Field_SQL)
    print(jk.get_string('Integer').render(max_len=1,default=0,verbose_name=None,primary_key=True,
                                        auto_increment=True))
    # jk.get_string(IntegerField_SQL[10001])
