from fastapi import FastAPI

app = FastAPI(title="Basic Api", description="This is the api built for the basic purpose", version='1.0.0')

# For homepage
@app.get('/')
def root_page()
    return {'message': "Welcome to the Homepage"}

# Taking the name in URL as the parameter
@app.get('/get/{name}')
def show_name(name):
    return {"message": f"Hellow {name}"}

# Post Endpoint -- taking the data
@app.post('/post')
def get_information(name, country):
    return {"message": f"Most Welcome {name} in the {country}"}

if __name__ =='__main__':
    import uvicorn
    uvicorn.run(app=)