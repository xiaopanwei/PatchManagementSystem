from db.db import get_connection
from modal import patchDetails


def findPatchById(patchId):
    conn = get_connection()
    cursor = conn.cursor()
    patch = patchDetails()
    sql = 'SELECT * FROM patch_details LEFT JOIN app_version ON patch_details.belong_app_version_code=app_version.version_code ' \
          'and patch_details.belong_app_id= app_version.app_id WHERE patch_id= %s'
    try:
        cursor.execute(sql, patchId)
        for c in cursor:
            patch.patchId = c['patch_id'] if c['patch_id'] is not None else ""
            patch.belongAppId = c['app_id'] if c['app_id'] is not None else ""
            patch.appVersionCode = c['version_code'] if c['version_code'] is not None else ""
            patch.appVersionName = c['version_name'] if c['version_name'] is not None else ""
            patch.patchVersion = c['patch_version'] if c['patch_version'] is not None else ""
            patch.patchSize = c['patch_size'] if c['patch_size'] is not None else ""
            patch.patchContent = c['patch_content'] if c['patch_content'] is not None else ""
            patch.updateTime = c['upload_time'] if c['upload_time'] is not None else ""
            patch.downLoadState = c['download_state'] if c['download_state'] is not None else ""
    finally:
        conn.close()
    return patch


def changeDownloadPatch(state, patchId):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE patch_details SET download_state= %s , patch_flag = 0 WHERE patch_id=%s "
    try:
        cursor.execute(sql, (state, patchId))
        conn.commit()
    finally:
        conn.close()

    return None


def delPatchByPatchId(patchId):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE patch_details SET patch_flag = 1 , download_state = 2 WHERE patch_id = %s"
    try:
        cursor.execute(sql, (patchId))
        conn.commit()
    finally:
        conn.close()
    return None
