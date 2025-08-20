import pymongo
import os
class DataLoader:
    def __init__(self):


        self.MONGO_USER = os.getenv("MONGO_USER", "root")
        self.MONGO_PASS = os.getenv("MONGO_PASS", "example")
        self.MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
        self.MONGO_PORT = os.getenv("MONGO_PORT", "27017")
        self.MONGO_DB = os.getenv("MONGO_DB", "enemy_soldiers")

        self.url = f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}"


    def get_all_data(self):
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.MONGO_DB]
        mycol = mydb["enemy_soldiers"]
        return list(mycol.find())

    def insert_data(self,ID,first_name,last_name,phone_number,rank):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.MONGO_DB]
        mycol = mydb["enemy_soldiers"]
        return {"status insert data:ok"}


    def update_data(self, ID, param):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.MONGO_DB]
        mycol = mydb["enemy_soldiers"]
        mycol.update_one({"ID": ID}, {"$set": param})
        return {"status update data: ok"}

    def delete_data(self,ID):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.MONGO_DB]
        mycol = mydb["enemy_soldiers"]
        mycol.delete_one({"ID": ID})
        return {"status delete data:ok"}