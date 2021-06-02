class lastVersion:
    def __init__(self):
        self.appId = ""
        self.appName = ""
        self.appLastVersionCode = ""
        self.appLastVersionName = ""
        self.patchLastVersionName = ""
        self.patchLastId = ""


class appLastPatchVersion:
    def __init__(self):
        self.appVersion = ''
        self.appVersionCode = ''
        self.patchVersion = ''
        self.updateTime = ''
        self.patchId = ''
        self.patchContent = ''

class patchDetails:
    def __init__(self):
        self.patchId = ''
        self.belongAppId=''
        self.appVersionCode = ''
        self.appVersionName = ''
        self.patchVersion = ''
        self.patchSize = ''
        self.patchContent = ''
        self.updateTime = ''
        self.downLoadState = ''


class ossModal:
    def __init__(self):
        self.keyId = "输入你的阿里云OSS keyid"
        self.keySecret = "输入你的阿里云OSS keySecret"
        self.url = "http://oss-cn-hangzhou.aliyuncs.com"
        self.public_url = "https://yourbucketname.oss-cn-hangzhou.aliyuncs.com/"


class db:
    def __init__(self):
        self.host = '输入你的云数据库host'
        self.user_name = '输入你的云数据库 账号'
        self.password = '输入你的云数据库 密码'
        self.db_name = '数据库名称'
