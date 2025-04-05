from pydantic import BaseModel

# Define a Pydantic model for a Note
class Note(BaseModel):
    title: str  # The title of the note, like the name of a book
    description: str  # The description of the note, like a summary
    Important: bool = True  # Indicates if the note is important, True by default
