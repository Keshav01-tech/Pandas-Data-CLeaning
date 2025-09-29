from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")
com = MongoClient("mongodb+srv://keshav_o1:keshav%40123@cluster0.brub8.mongodb.net/notes")
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = com.notes.notes.find({})
    newDocs =[]
    for doc in docs:
        newDocs.append({"id": doc["_id"],
                        "note":doc["note"] })
    return templates.TemplateResponse("index.html",  {"request" :request, "newDocs":newDocs})



@app.get("/items/{item_id}")
def read_item(item_id: int, q:str|None = None):

    return {"item_id": item_id, "q": q}
