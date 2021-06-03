from db.db import get_connection
from time import strftime

def findVersionNameByCodeAndId(appId, appVersionCode):
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT version_name FROM app_version WHERE app_id= %s AND version_code=%s'
    appVersionName = ''
    try:
        cursor.execute(sql, (appId, appVersionCode))
        for c in cursor:
            appVersionName = c['version_name'] if c['version_name'] is not None else ""
    finally:
        conn.close()
    return appVersionName


def publishPatchUtil(appId,appVersionCode,patch_url,patch_content,patch_version,patch_size):
    conn = get_connection()
    cursor = conn.cursor()
    nowTime=strftime("%Y-%m-%d %H:%M")
    sql='INSERT  INTO patch_details (belong_app_id,belong_app_version_code,patch_download_url,patch_content,patch_version,' \
        'patch_size,download_state,upload_time,patch_flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,0)'
    try:
        cursor.execute(sql, (appId,appVersionCode,patch_url,patch_content,patch_version,patch_size,0,nowTime))
        conn.commit()
    finally:
        conn.close()


def getPatchList(appId,appVersion):
    conn = get_connection()
    cursor = conn.cursor()
    patchList=[]
    sql="SELECT * FROM patch_details WHERE belong_app_id=%s AND belong_app_version_code=%s AND download_state=1 AND patch_flag=0"
    try:
        cursor.execute(sql, (appId, appVersion))
        for c in cursor:
            patchList.append(c['patch_download_url'])
    finally:
        conn.close()
    return patchList