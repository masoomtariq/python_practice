from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app with metadata
app = FastAPI(
    title="Basic API", 
    description="This is the API built for basic purposes", 
    version="1.0.0"
)

# ----------------------------- Routes -----------------------------

# Root route - Home page
@app.get('/')
def root_page():
    # Returns a welcome message at the base URL
    return {'message': "Welcome to the Homepage"}

# GET endpoint with a path parameter
@app.get('/get/{name}')
def show_name(name: str):
    # Returns a personalized greeting
    return {"message": f"Hello {name}"}

# POST endpoint that receives JSON data using a Pydantic model
@app.post('/post')
def get_information(name: str, country: str):
    # Access data from the request body using dot notation
    return {"message": f"Most Welcome {name} in the {country}"}

# ----------------------------- Server Runner -----------------------------

# This allows running the app directly with Python (useful in dev mode)
if __name__ == "__main__":
    import uvicorn
    # The filename should match this script's name, e.g., basic_apis.py
    uvicorn.run("fast_api:app", reload=True)