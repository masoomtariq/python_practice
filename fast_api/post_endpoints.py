from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

description = "This is the testing api that specially build for the post_endpoint. In this Endpoint, Try registering users and catching duplicate usernames!"

users_db = {}

app = FastAPI(title="Post_api", description= description, version="1.0.0")

@app.post('/item1')
def create_items1(name: str, price: int, in_stock: Optional[bool] = True):
    return {"Recieved": {'name': name, 'price': price, 'in_stock': in_stock}}

class Item(BaseModel):
    name : str
    price: int
    in_stock : Optional[bool]

@app.post('/item2')
def create_items2(item: Item):
    return {"Recieved": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("post_endpoints:app", reload=True)