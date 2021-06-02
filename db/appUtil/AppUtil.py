from db.db import get_connection
from modal import lastVersion

# 获取每个App最新版本的最新补丁
# 使用了开窗函数
def getLastVersion():
    conn = get_connection()
    cursor = conn.cursor()
    detailsList = []
    sql = "SELECT * FROM(SELECT app.app_id,app.app_name,app_version.version_code,app_version.version_name, " \
          "patch_details.patch_id,patch_details.patch_version," \
          "rank ( ) over ( PARTITION BY app.app_id ORDER BY app_version.version_code DESC, patch_details.patch_id DESC ) AS ra " \
          "FROM app LEFT JOIN app_version ON app.app_id = app_version.app_id " \
          "LEFT JOIN patch_details ON app_version.version_code = patch_details.belong_app_version_code " \
          "WHERE app.app_flag = 0)" \
          " tmp WHERE tmp.ra = 1"
    try:
        cursor.execute(sql)
        for c in cursor:
            details = lastVersion()
            details.appId = c['app_id']
            details.appName = c['app_name']
            details.patchLastId = c['patch_id']
            details.appLastVersionName = c['version_name']
            details.appLastVersionCode = c['version_code']
            details.patchLastVersionName = c['patch_version']
            detailsList.append(details)

    finally:
        conn.close()
    return detailsList


def addAppName(appName):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO app (app_name) VALUES (%s)"
    try:
        cursor.execute(sql, (appName))
        conn.commit()
    finally:
        conn.close()


def addAppVersion(appId,appVersionName,appVersionCode):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO app_version (app_id,version_code,version_name) VALUES (%s,%s,%s)"
    try:
        cursor.execute(sql, (appId,appVersionName,appVersionCode))
        conn.commit()
    finally:
        conn.close()