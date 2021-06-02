from flask import Flask

from appSettingPackage import appSetting
from patchPackage import patch
from publishPatchPackage import publishPatch

app = Flask(__name__)
from patchDetailsPackage import patchDetails
from loginPackage import login
# 必须注册蓝图，否则找不到页面
app.register_blueprint(login.loginBlueprint)
app.register_blueprint(patchDetails.patchDetailsBlueprint)
app.register_blueprint(appSetting.appSettingBlueprint)
app.register_blueprint(patch.patchBlueprint)
app.register_blueprint(publishPatch.publishPatchBlueprint)
app.secret_key = 'patch'

@app.route("/")
def index():
    return login.loginIndex()


if __name__ == "__main__":
    app.run(debug=True)






