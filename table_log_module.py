import mysql_module
import db_config

# 全局变量
flag = False

def create_table_log(): #创建记录表，如果有则不创建
    global flag
    if not flag:
        db = mysql_module.connect(*db_config.get_db_config())
        try:
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'table_log'")
            result = cursor.fetchone()
            if result[0] == 0:
                cursor.execute(f"""
                CREATE TABLE table_log (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """)
                db.commit()
                print(f"数据表 'table_log' 创建成功")
            else:
                print(f"数据表 'table_log' 已存在")
            flag = True
        except Exception as e:
            print(f"发生错误: {e}")
            db.rollback()
        finally:
            db.close()
