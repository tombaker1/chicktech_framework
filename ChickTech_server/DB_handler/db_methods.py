from pymongo import MongoClient

class DBManager():
    collection = None
    def __init__(self):
        # The DB is assumed to be running on LocalHost
        client = MongoClient('localhost', 27017)
        db = client.ChickTechDB
        self.collection = db.users


    def insertProfile (self, profile):
        try:
            ret = self.collection.insert_one(profile).inserted_id
            print(ret)

        except Exception as E:
            print(E)
