from fastapi import FastAPI
from dal import DataLoader as dl
import soldiers
from pydantic import BaseModel

app = FastAPI()



@app.post("/POST")
async def create_item(ID,first_name,last_name,phone_number,rank):
    dl.insert_data(ID,first_name,last_name,phone_number,rank)

@app.get("/GET")
async def read_item():
    return dl.get_all_data()


@app.put("/PUT")
async def update_item(ID,param):
    dl.update_data(ID,param)


@app.delete("/DELETE")
async def delete_item(ID):
    dl.delete_data(ID)
    return {"message": "Item deleted successfully"}