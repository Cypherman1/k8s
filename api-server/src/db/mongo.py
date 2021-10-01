from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
from datetime import datetime, time, timedelta
import pytz

load_dotenv()
try:
    client = MongoClient(os.environ.get("MONGO_URI"), serverSelectionTimeoutMS=1000)
    db = client["sa-db"]
    client.server_info()
except:
    print("Error - Can not connect to DB!")


def getAllSessions():
    try:
        collection = db["session-logs"]
        return list(collection.find({}))
    except Exception as ex:
        print(f"Erorr - {ex}")


def logSession(user, number):
    try:

        collection = db["session-logs"]
        post = {"user": user, "number": number, "datetime": datetime.now() + timedelta(hours=7)}
        return collection.insert_one(post)
    except Exception as ex:
        print(f"Erorr - {ex}")
