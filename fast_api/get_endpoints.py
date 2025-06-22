from fastapi import FastAPI

app = FastAPI(title="Basic api", description="THis api is mainly build for testing", version = '1.0.0')

@app.get('/')
def main():
    return {'message': "This is the home Page"}

@app.get("/items/{item_id}")
def read_item1(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("get_endpoints:app", reload=True, port=8001)