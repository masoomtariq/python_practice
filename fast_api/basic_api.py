from fastapi import FastAPI

app = FastAPI(title="Basic api", description="THis api is mainly build for testing", version = '1.0.0')

@app.get('/')
def main():
    return {'message': "this is my first api"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("basic_api:app", reload=True)