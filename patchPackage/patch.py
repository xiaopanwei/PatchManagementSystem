from flask import Blueprint, render_template, session

from db.pathUtil import PatchUtil

patchBlueprint = Blueprint("patch", __name__, static_folder="static", template_folder="template",
                            url_prefix="/patch")

@patchBlueprint.route("/<appId>")
def patchIndex(appId):
    name = session.get('username')
    lastPatchList = PatchUtil.getAppLastPtachList(appId)
    return render_template("patch.html",name=name,appId=appId,lastPatchList=lastPatchList)

@patchBlueprint.route("/historyPatch/<appId>")
def historyPatch(appId):
    name = session.get('username')
    historyPatchList=PatchUtil.findHistoryPatchList(appId)
    print(historyPatchList)
    return render_template("historyPatch.html",name=name,appId=appId,historyPatchList=historyPatchList)
