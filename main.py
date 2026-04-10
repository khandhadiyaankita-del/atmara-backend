from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

app = FastAPI()

origins = [
    "https://nimble-melomakarona-1d767c.netlify.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["atmara"]
collection = db["entries"]

@app.get("/")
def home():
    return {"status": "ATMARA backend running"}

@app.post("/add")
def add_entry(data: dict):
    collection.insert_one(data)
    return {"message": "Data added successfully"}

@app.get("/all")
def get_all():
    data = list(collection.find({}, {"_id": 0}))
    return data
