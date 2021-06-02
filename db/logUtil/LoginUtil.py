from db.db import get_connection


def user_check(username,password):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT count(*) FROM web_user WHERE user_name=%s and password=%s and flag=0"
    try:
        cursor.execute(sql, (username,password))
        for c in cursor:
            count = c['count(*)']

    finally:
        conn.close()
    return count
