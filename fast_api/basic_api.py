from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Basic api", description="THis api is mainly build for testing", version = '1.0.0')

@app.get('/')
def main():
    return {'message': "this is my first api"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run("basic_api:app", reload=True)