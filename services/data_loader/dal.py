import pymongo
import os
class DataLoader:
    def __init__(self):


        self.MONGO_USER = os.getenv("MONGO_USER", "root")
        self.MONGO_PASS = os.getenv("MONGO_PASS", "example")
        self.MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
        self.MONGO_PORT = os.getenv("MONGO_PORT", "27017")
        self.MONGO_DB = os.getenv("MONGO_DB", "enemy_soldiers")

        url = f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}"
        - MONGO_INITDB_ROOT_USERNAME =$MONGO_INITDB_ROOT_USERNAME
        - MONGO_INITDB_ROOT_PASSWORD =$MONGO_INITDB_ROOT_PASSWORD
        - APP_USER =$APP_USER
        - APP_PWD =$APP_PWD
        - DB_NAME =$DB_NAME
        - DB_COLLECTION_NAME =$DB_COLLECTION_NAME
        - MONGO_HOSTNAME =$MONGO_HOSTNAME

    def get_all_data(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]

    def insert_data(self,ID,first_name,last_name,phone_number,rank):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        return {"status insert data:ok"}

    def update_data(self,ID,param):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        return {"status update data:ok"}

    def delete_data(self,ID):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        return {"status delete data:ok"}