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
            # ret = self.collection.insert_one(profile).inserted_id
            # print(ret)
            self.collection.insert(profile)

        except Exception as E:
            print(E.args)

    def listProfiles(self):
        profileList = []
        try:
            for doc in self.collection.find():
                print(doc)
                profileList.append(doc)
            return profileList

        except Exception as E:
            print(E.args)

    def listDesiredProfiles(self, filters):
        profileList = []
        try:
            for filter in filters:
                profileList.append(self.collection.find(filter))
            return profileList

        except Exception as E:
            print(E.args)