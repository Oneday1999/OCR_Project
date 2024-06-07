import mysql.connector
import uuid
import db_config
import sql_queries

def connect(host, user, password, database): #连接数据库
    try:
        db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
    except Exception as e:
        exit(1)
    else:
        return db

def create_table_name(texts): #为每一名用户创建数据表，表名为“user_姓名_加密随机数”
    name = next((item.split('姓名：')[1] for item in texts if '姓名：' in item), None)
    if name is None:
        name = "未识别姓名"
    id = uuid.uuid1().hex
    table_name = f"user_{name}_{id[:12]}"
    return table_name
        
def insert(texts, image_path): #插入识别到的数据
    db = connect(*db_config.get_db_config())
    table_name = create_table_name(texts)
    try:
        # 读取图片文件
        with open(image_path, 'rb') as file:
            binary_data = file.read()
    except Exception as e:
        print(f"发生错误: {e}")
        db.close()
        exit(1)

    try:
        cursor = db.cursor()
        cursor.execute(sql_queries.create_table_queries (table_name)) #在sql执行创建数据表任务
        cursor.execute(sql_queries.table_log_queries(table_name)) #在sql执行插入记录任务
        cursor.execute(sql_queries.insert_data(texts, table_name, binary_data)) #在sql执行插入数据任务
        db.commit()
    except Exception as e:
        print(f"发生错误: {e}")
        db.rollback()
        db.close()
        exit(1)
    else:
        print(f"数据表 '{table_name}' 创建成功")
        db.close()