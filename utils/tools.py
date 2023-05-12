import re


# 转成更新SQL语句转换data方法
def to_update_sql_type_param(model):
    dict_data = model.dict(exclude_unset=True)
    del dict_data['id']
    str_param = str(dict_data)[1:-1]
    sql_param = re.sub(r"\'(\w+)\':", r"\1=", str_param)
    return str(sql_param)
