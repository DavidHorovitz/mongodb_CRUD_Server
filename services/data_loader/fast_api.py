from fastapi import FastAPI
import dal
from services.data_loader.dal import DataLoader

app = FastAPI()



@app.post("/POST")
async def create_item():
    dal = DataLoader()
    dal.insert_data(ID,first_name,last_name,phone_number,rank)

@app.get("/GET")
async def read_item():
    dal = DataLoader()
    gety=dal.get_all_data()
    return gety

@app.put("/PUT")
async def update_item():
    dal = DataLoader()
    dal.update_data(id,param)


@app.delete("/DELETE")
async def delete_item(item_id: int):
    dal = DataLoader()
    dal.delete_data(id)
    return {"message": "Item deleted successfully"}