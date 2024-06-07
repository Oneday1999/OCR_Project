import helper_function_module
import base64

def create_table_queries(table_name): #为每一名用户创建数据表
    return f"""CREATE TABLE {table_name} (
        ID号 VARCHAR(50),
        提取项目 TEXT,
        报告图片 LONGBLOB);"""

def table_log_queries(table_name): #记录每一名用户的表名
    return f"""INSERT INTO table_log (user_name)
        VALUES ('{table_name}');"""

def insert_data(tests, table_name, binary_data):
    tests_str = ', '.join(map(str, tests))
    id = helper_function_module.find_ID(tests)

    # 将二进制数据转换为base64编码的字符串
    binary_data_base64 = base64.b64encode(binary_data).decode()

    return f"""INSERT INTO {table_name} (ID号, 提取项目, 报告图片)
        VALUES ('{id}', '{tests_str}', FROM_BASE64('{binary_data_base64}'));""" #在数据库插入id号，提取项目，报告图片