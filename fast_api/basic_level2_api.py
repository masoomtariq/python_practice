from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Basic Api", description= "This is the basic api on level 02", version="1.0.0")

@app.post('/item1')
def create_items1(name: str, price: int, in_stock: bool = True):
    return {"Recieved": {'name': name, 'price': price, 'in_stock': in_stock}}

class Item(BaseModel):
    name : str
    price: int
    in_stock : Optional[bool] = True

@app.post('/item2')
def create_items2(item: Item):
    return {"Recieved": item}