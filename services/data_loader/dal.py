import pymongo
import os
class DataLoader:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "mysql")
        self.user = os.getenv("DB_USER", "appuser")
        self.password = os.getenv("DB_PASSWORD", "appPass123!")
        self.database = os.getenv("DB_NAME", "datadb")


        MONGO_INITDB_ROOT_USERNAME =$MONGO_INITDB_ROOT_USERNAME
        MONGO_INITDB_ROOT_PASSWORD =$MONGO_INITDB_ROOT_PASSWORD
        APP_USER =$APP_USER
        APP_PWD =$APP_PWD
        DB_NAME =$DB_NAME
        DB_COLLECTION_NAME =$DB_COLLECTION_NAME
        MONGO_HOSTNAME =$MONGO_HOSTNAME
        return

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