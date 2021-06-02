from flask import Blueprint, render_template, session, redirect, url_for, request

from db.appUtil import AppUtil
from db.appUtil.AppUtil import getLastVersion

appSettingBlueprint = Blueprint("appSetting", __name__, static_folder="static", template_folder="template",
                                url_prefix="/appSetting")


@appSettingBlueprint.route("/")
def appSettingIndex():
    name = session.get('username')
    patchList = getLastVersion()
    return render_template("appSetting.html", name=name, patchList=patchList)


@appSettingBlueprint.route("/addAppName")
def addAppName():
    name = session.get('username')
    return render_template("addAppName.html", name=name)


@appSettingBlueprint.route("/doAddAppName", methods=['POST', 'GET'])
def doAddAppName():
    appName = request.args.get('app_name')
    AppUtil.addAppName(appName)
    return redirect(url_for('appSetting.addAppName'))


@appSettingBlueprint.route("/addAppVersion/<appId>")
def addAppVersion(appId):
    name = session.get('username')
    return render_template("addAppVersion.html", name=name, appId=appId)


@appSettingBlueprint.route("/doAddAppVersion/<appId>", methods=['POST', 'GET'])
def doAddAppVersion(appId):
    appVersion = request.args.get('app_version')
    appName = request.args.get('app_name')
    AppUtil.addAppVersion(appId, appVersion, appName)
    return redirect(url_for('patch.patchIndex', appId=appId))
