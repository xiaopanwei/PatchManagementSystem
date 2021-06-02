import pymysql.cursors

from modal import db


def get_connection():
    dbInfo = db()
    connection = pymysql.connect(
        host=dbInfo.host, port=3306,
        user=dbInfo.user_name,
        password=dbInfo.password,
        db=dbInfo.db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection
