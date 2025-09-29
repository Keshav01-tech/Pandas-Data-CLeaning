from fastsapi import FastAPI
from routes.note import Note
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(Note)