from flask import Blueprint, render_template, session, redirect, url_for

from db.patchDetailsUtil.PatchDetailsUtil import findPatchById, changeDownloadPatch, delPatchByPatchId

patchDetailsBlueprint = Blueprint("patchDetails", __name__, static_folder="static", template_folder="template",
                                  url_prefix="/details")


@patchDetailsBlueprint.route("/<patchId>")
def patchDetailsIndex(patchId):
    name = session.get('username')
    patchDetails= findPatchById(patchId)
    print(patchDetails.patchId)
    return render_template("patchDetails.html",name=name,patchDetails=patchDetails)

@patchDetailsBlueprint.route("/changeDownload/<state>/<patchId>")
def changeDownload(state,patchId):
    changeDownloadPatch(state,patchId)
    return redirect(url_for('patchDetails.patchDetailsIndex', patchId=patchId))

@patchDetailsBlueprint.route("/delPatch/<patchId>")
def delPatch(patchId):
    delPatchByPatchId(patchId)
    return redirect(url_for('patchDetails.patchDetailsIndex', patchId=patchId))
