from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Blog Post", description="This is the api that is used to create a blog post", version='1.0.0')

@app.get('/')
def root_page():
    return {"message": "Welcome to the Homepage."}

class Blog(BaseModel):
    title : str
    content : str
    tags : Optional[List[str]] = []
    maetadata : Optional[dict]

@app.post('/blog_post')
def create_blog(blog : Blog):
    if not blog.title or blog.content:
        raise HTTPException(status_code=400, detail="Title and the content are required")
    
    