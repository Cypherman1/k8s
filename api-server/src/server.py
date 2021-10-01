from flask import Flask, Response, request, jsonify
from werkzeug.datastructures import ContentSecurityPolicy
from db.mongo import logSession, getAllSessions
import json
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)


fileDir = "/usr/mydata/version.txt"


@app.route("/get-version", methods=["GET"])
@cross_origin(supports_credentials=True)
def getVersion():
    try:
        f = open(fileDir, "r")
        version = f.readline()
        f.close()
        return Response(
            response=json.dumps({"message": "success", "version": f"{version}"}),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "failed"}), status=500, mimetype="application/json")


@app.route("/get-info", methods=["GET"])
@cross_origin(supports_credentials=True)
def getInfo():
    try:
        allInfo = getAllSessions()
        print(allInfo)
        for item in allInfo:
            item["_id"] = str(item["_id"])
            item["datetime"] = item["datetime"].strftime("%m/%d/%Y, %H:%M:%S")
        return Response(response=json.dumps(allInfo), status=200, mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "failed"}), status=500, mimetype="application/json")


@app.route("/log-session", methods=["POST"])
def log():
    try:
        # print(request.data.name)
        dbRes = logSession(request.json["name"], request.json["number"])
        return Response(
            response=json.dumps({"message": "success", "data": f"{dbRes.inserted_id}"}),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "failed"}), status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5555", debug=True)

# logSession("nttung2")
