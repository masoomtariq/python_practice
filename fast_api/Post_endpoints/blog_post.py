from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Blog Post", description="This is the api that is used to create a blog post", version='1.0.0')

@app.get('/')
def root_page():
    return {"message": "Welcome to the Homepage."}

class bloge(BaseModel):
    title : str
    content : str
    tags : Optional[list]
    maetadata : Optional[dict]