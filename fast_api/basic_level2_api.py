from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Basic Api", description= "This is the basic api on level 02", version="1.0.0")
