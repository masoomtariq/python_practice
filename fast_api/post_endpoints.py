from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

description = "This is the testing api that specially build for the post_endpoint. In this Endpoint, Try registering users and catching duplicate usernames!"

users_db = {}

app = FastAPI(title="Post_api", description= description, version="1.0.0")

@app.get('/')
def root_page():
    return {"message": f"Welcome to the Homepage. {description}"}

class user(BaseModel):
    username: str
    email: EmailStr
    FullName: Optional[str] = None

@app.post('/register')
def register_user(User: user):
    if User.username in users_db or User.FullName in users_db:
        raise HTTPException(status_code=400, detail="The given username or the Fullname already Exist.")
    users_db[User.username] = User
    return {"message": f"The user'{User.username}' registered successfully.", "User": User}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("post_endpoints:app", reload=True)