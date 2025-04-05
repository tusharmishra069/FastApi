from fastapi import FastAPI  # Importing FastAPI to create the app
from routes.note import note  # Importing the note router from routes
from fastapi.staticfiles import StaticFiles  # For serving static files
from fastapi.templating import Jinja2Templates  # For using templates

app = FastAPI()  # Making a FastAPI app
app.mount("/static", StaticFiles(directory="static"), name="static")  # Adding a folder for static files
templates = Jinja2Templates(directory="templates")  # Setting up templates folder
app.include_router(note)  # Adding the note router to the app