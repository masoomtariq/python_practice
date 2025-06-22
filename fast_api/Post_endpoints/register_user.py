from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

description = "This is the testing api that specially build for the post_endpoint. In this Endpoint, Try registering users and catching duplicate usernames!"

users_db = {}

app = FastAPI(title="Post_api", description= description, version="1.0.0")

@app.get('/')
def root_page():
    return {"message": f"Welcome to the Homepage. {description}"}

class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str

@app.post('/register', response_model= dict)
def register_user(User: RegisterUser) -> dict:
    username = User.username
    if username in users_db:
        raise HTTPException(status_code=400, detail=f"The given username '{username}' already Exist.")
    
    users_db[username] = User
    return {
        "message": f"User '{username}' registered successfully.",
        "user": User.model_dump(exclude={"password"})  # Do NOT return the password
    }

class LoginUser(BaseModel):
    username: str
    password: str

@app.post('/login', response_model=dict)
def login_user(user: LoginUser) -> dict:

    username = user.username
    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid username")

    elif users_db.get(username)['password'] != user.password:
        raise HTTPException(status_code=401, detail="Ivalid Password")
    
    return {"message": f"Welcome back, {user.username}!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("register_user:app", reload=True)