from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity
from fastapi.templating import Jinja2Templates

# Make a router for notes
note = APIRouter()
# Tell it where the templates live
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item_html(request: Request):
    """
    Handles GET requests to fetch and display notes.
    """
    # Get all the notes from the database
    docs = conn.notes.notes.find({})
    newDocs = []
    # Go through each note and make it look nice
    for doc in docs:
        newDocs.append({
            "id": doc.get("_id"),  # Get the ID of the note
            "title": doc.get("title", "Untitled"),  # If no title, call it "Untitled"
            "description": doc.get("description", "No description"),  # If no description, say "No description"
            "Important": doc.get("Important", False),  # Is it important? Default is False
        })
    # Show the notes on the webpage
    return templates.TemplateResponse(
        name="index.html", context={"request": request, "newDocs": newDocs}
    )

@note.post("/add_note")
async def add_note(note: Note):
    """
    Handles POST requests to add a new note using JSON payload.
    """
    # Add the new note to the database
    inserted_note = conn.notes.notes.insert_one(dict(note))
    # Return the note back
    return noteEntity(inserted_note)

@note.post("/create_item")
async def create_item(request: Request):
    """
    Handles POST requests to create a new note using form data.
    """
    # Get the form data from the user
    form = await request.form()
    formDict = dict(form)
    # Check if the "Important" checkbox is on
    formDict["Important"] = "true" if formDict.get("Important") == "on" else "false"
    # Add the form data as a new note in the database
    conn.notes.notes.insert_one(formDict)
    # Tell the user it worked
    return {"Success": True}