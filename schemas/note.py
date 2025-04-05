# This function takes a single note item and converts it into a dictionary
def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),  # Convert the note's ID to a string
        "title": item["title"],  # Get the title of the note
        "description": item["description"],  # Get the description of the note
        "Important": item["Important"],  # Check if the note is important
    }

# This function takes a list of notes and converts each one using noteEntity
def notesEntity(entity) -> list:
    return [noteEntity(item) for item in entity]  # Loop through all notes and convert them