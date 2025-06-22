from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Item Shop", description="This is the api that is used to create a order products", version='1.0.0')

products_db = {
    1: {"name": "Book", "price": 500},
    2: {"name": "Pen", "price": 100},
    3: {"name": "Laptop", "price": 100000},
}

orders_db = []

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class OrderRequest(BaseModel):
    customer_id: int
    items: List[OrderItem]
    note: str = ""

