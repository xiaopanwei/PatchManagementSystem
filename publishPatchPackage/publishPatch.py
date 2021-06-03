import calendar
import time
import math
import oss2 as oss2
from flask import Blueprint, render_template, session, request, redirect, url_for, jsonify
from itsdangerous import json

from db.publishPatchUtil.PublishPatchUtil import findVersionNameByCodeAndId, publishPatchUtil, getPatchList
from modal import ossModal

publishPatchBlueprint = Blueprint("publishPatch", __name__, static_folder="static", template_folder="template",
                                  url_prefix="/publish")


@publishPatchBlueprint.route("/newPatch/<appId>/<appVersionCode>")
def publishPatchIndex(appId, appVersionCode):
    name = session.get('username')
    appVersionName = findVersionNameByCodeAndId(appId, appVersionCode)
    return render_template("publishPatch.html", name=name, appId=appId, appVersionCode=appVersionCode,
                           appVersionName=appVersionName)


@publishPatchBlueprint.route("/submitPatch", methods=['GET', 'POST'])
def submitPatch():
    appId = request.args.get('appId')
    appVersionCode = request.args.get('appVersionCode')
    patch_url = request.args.get('patch_url')
    patch_content = request.args.get('patch_content')
    patch_version = request.args.get('patch_version')
    patch_size = request.args.get('patch_size')
    patch_size=bit_conversion(patch_size)
    publishPatchUtil(appId, appVersionCode, patch_url, patch_content, patch_version,patch_size)
    return redirect(url_for('patch.patchIndex', appId=appId))


@publishPatchBlueprint.route("/uploadPatch", methods=['GET', 'POST'])
def uploadPatch():
    if request.method == 'POST':
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的文件类型，仅限于patch", "patch_size": 0})
        ossmodal = ossModal()
        # 秒级时间戳
        imagename = "patch" + str(calendar.timegm(time.gmtime())) + "." + f.filename.rsplit('.', 1)[1]
        auth = oss2.Auth(ossmodal.keyId, ossmodal.keySecret)
        bucket = oss2.Bucket(auth, ossmodal.url, "xpw-patch")
        # 查看阿里云官方文档
        bucket.put_object(imagename, f)
        return jsonify({"error": 0, "msg":ossmodal.public_url + imagename,
                        "patch_size": bucket.get_object_meta(imagename).headers['Content-Length']})

# 根据appid以及app版本号获得补丁下载地址
@publishPatchBlueprint.route("/getPatch",methods=['POST','GET'])
def bugDetailUpdate():
    appId=request.args.get('app_id')
    appVersion=request.args.get('app_version')
    patchList=getPatchList(appId,appVersion)
    # 使用lambda序列化
    data = json.dumps({"patchList": patchList}, default=lambda obj: obj.__dict__,
                      sort_keys=False)

    return data

# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['patch'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#字节转换为文件大小
def bit_conversion(size, dot=2):
    size = float(size)
    # 位 比特 bit
    if 0 <= size < 1:
        human_size = str(round(size / 0.125, dot)) + ' b'
    # 字节 字节 Byte
    elif 1 <= size < 1024:
        human_size = str(round(size, dot)) + ' B'
    # 千字节 千字节 Kilo Byte
    elif math.pow(1024, 1) <= size < math.pow(1024, 2):
        human_size = str(round(size / math.pow(1024, 1), dot)) + ' KB'
    # 兆字节 兆 Mega Byte
    elif math.pow(1024, 2) <= size < math.pow(1024, 3):
        human_size = str(round(size / math.pow(1024, 2), dot)) + ' MB'
    # 吉字节 吉 Giga Byte
    elif math.pow(1024, 3) <= size < math.pow(1024, 4):
        human_size = str(round(size / math.pow(1024, 3), dot)) + ' GB'
    # 太字节 太 Tera Byte
    elif math.pow(1024, 4) <= size < math.pow(1024, 5):
        human_size = str(round(size / math.pow(1024, 4), dot)) + ' TB'
    # 拍字节 拍 Peta Byte
    elif math.pow(1024, 5) <= size < math.pow(1024, 6):
        human_size = str(round(size / math.pow(1024, 5), dot)) + ' PB'
    # 艾字节 艾 Exa Byte
    elif math.pow(1024, 6) <= size < math.pow(1024, 7):
        human_size = str(round(size / math.pow(1024, 6), dot)) + ' EB'
    # 泽它字节 泽 Zetta Byte
    elif math.pow(1024, 7) <= size < math.pow(1024, 8):
        human_size = str(round(size / math.pow(1024, 7), dot)) + ' ZB'
    # 尧它字节 尧 Yotta Byte
    elif math.pow(1024, 8) <= size < math.pow(1024, 9):
        human_size = str(round(size / math.pow(1024, 8), dot)) + ' YB'
    # 千亿亿亿字节 Bront Byte
    elif math.pow(1024, 9) <= size < math.pow(1024, 10):
        human_size = str(round(size / math.pow(1024, 9), dot)) + ' BB'
    # 百万亿亿亿字节 Dogga Byte
    elif math.pow(1024, 10) <= size < math.pow(1024, 11):
        human_size = str(round(size / math.pow(1024, 10), dot)) + ' NB'
    # 十亿亿亿亿字节 Dogga Byte
    elif math.pow(1024, 11) <= size < math.pow(1024, 12):
        human_size = str(round(size / math.pow(1024, 11), dot)) + ' DB'
    # 万亿亿亿亿字节 Corydon Byte
    elif math.pow(1024, 12) <= size:
        human_size = str(round(size / math.pow(1024, 12), dot)) + ' CB'
    # 负数
    else:
        raise ValueError('bit_conversion Error')
    return human_size