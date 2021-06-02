from db.db import get_connection
from modal import appLastPatchVersion


# 获取每个版本的最新补丁
def getAppLastPtachList(appId):
    conn = get_connection()
    cursor = conn.cursor()
    lastPatchList = []
    sql = "SELECT * FROM ( SELECT *, rank ( ) over ( PARTITION BY app_version.version_code ORDER BY patch_details.patch_id DESC ) AS ra " \
          "FROM app_version LEFT JOIN patch_details ON app_version.app_id = patch_details.belong_app_id " \
          "AND app_version.version_code = patch_details.belong_app_version_code " \
          "WHERE app_id = %s AND app_version.version_flag = 0 " \
          ") tmp WHERE tmp.ra = 1 ORDER BY version_code DESC"
    try:
        cursor.execute(sql, appId)
        for c in cursor:
            patchVersion = appLastPatchVersion()
            # 类似三木运算符，判断是否为空为空显示“”
            patchVersion.appVersion = c['version_name'] if c['version_name'] is not None else ""
            patchVersion.appVersionCode = c['version_code'] if c['version_code'] is not None else ""
            patchVersion.patchVersion = c['patch_version'] if c['patch_version'] is not None else ""
            patchVersion.updateTime = c['upload_time'] if c['upload_time'] is not None else ""
            patchVersion.patchId = c['patch_id'] if c['patch_id'] is not None else ""
            lastPatchList.append(patchVersion)
    finally:
        conn.close()
    return lastPatchList


def findHistoryPatchList(appId):
    conn = get_connection()
    cursor = conn.cursor()
    patchList = {"versions":[],"versionList":{}}

    sql = "SELECT * , rank ( ) over ( PARTITION BY app_version.version_code ORDER BY patch_details.patch_id DESC ) AS ra " \
          "FROM app_version " \
          "LEFT JOIN patch_details ON app_version.app_id = patch_details.belong_app_id " \
          "AND app_version.version_code = patch_details.belong_app_version_code " \
          "WHERE app_id = %s " \
          "AND app_version.version_flag = 0 " \
          "ORDER BY version_code DESC"
    try:
        cursor.execute(sql, appId)
        for c in cursor:
            if patchList['versions'].count(c['version_name'])==0:
                patchList['versions'].append(c['version_name'])
                versionInfo = {str(c['version_name']):[]}
                if c['patch_id'] is not None:
                    patchVersion = appLastPatchVersion()
                    # 类似三木运算符，判断是否为空为空显示“”
                    patchVersion.appVersion = c['version_name'] if c['version_name'] is not None else ""
                    patchVersion.appVersionCode = c['version_code'] if c['version_code'] is not None else ""
                    patchVersion.patchVersion = c['patch_version'] if c['patch_version'] is not None else ""
                    patchVersion.updateTime = c['upload_time'] if c['upload_time'] is not None else ""
                    patchVersion.patchId = c['patch_id'] if c['patch_id'] is not None else ""
                    patchVersion.patchContent = c['patch_content'] if c['patch_content'] is not None else ""
                    versionInfo[str(c['version_name'])].append(patchVersion)
                    patchList['versionList'].update(versionInfo)
            else:
                if c['patch_id'] is not None:
                    patchVersion = appLastPatchVersion()
                    # 类似三木运算符，判断是否为空为空显示“”
                    patchVersion.appVersion = c['version_name'] if c['version_name'] is not None else ""
                    patchVersion.appVersionCode = c['version_code'] if c['version_code'] is not None else ""
                    patchVersion.patchVersion = c['patch_version'] if c['patch_version'] is not None else ""
                    patchVersion.updateTime = c['upload_time'] if c['upload_time'] is not None else ""
                    patchVersion.patchId = c['patch_id'] if c['patch_id'] is not None else ""
                    patchVersion.patchContent = c['patch_content'] if c['patch_content'] is not None else ""
                    patchList['versionList'][str(c['version_name'])].append(patchVersion)
    finally:
        conn.close()
    return patchList