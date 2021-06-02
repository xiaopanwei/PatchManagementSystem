from flask import Blueprint, render_template, session, redirect, url_for

from db.logUtil import LoginUtil

loginBlueprint = Blueprint("login", __name__, static_folder="static", template_folder="template",
                           url_prefix="/login")


@loginBlueprint.route("/")
def loginIndex():
    return render_template("login.html")


@loginBlueprint.route("/loginResult/<username>/<password>", methods=['POST'])
def loginResult(username,password):
    if int(LoginUtil.user_check(username,password)) > 0:
        return '{"state":0,"msg":"账号密码正确"}'
    else:
        return '{"state":1,"msg":"账号密码不正确"}'


@loginBlueprint.route("/loginSucess/<username>")
def loginSucess(username):
    session['username'] = username
    return redirect(url_for('appSetting.appSettingIndex'))


@loginBlueprint.route("/logout")
def loginOut():
    session['username'] = ""
    return redirect(url_for('login.loginIndex'))

