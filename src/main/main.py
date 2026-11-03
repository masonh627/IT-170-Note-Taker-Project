# Title: Note Building Project.
# Description: Tool that helps the user take and store notes.
# Authors: Manuel G, Carlos G, Mason H, Christian L, Elijah M, Jacobi T.

# This will be our main python script.

# Needed for naming the notes files
from datetime import datetime

# Function to handle saving the notes.
def saveNote(noteData: str, noteFileName:str =None, saveLocation:str =None) -> bool:
    """Writes note information out to a text file.
    
    Args:
        noteData: The string of data that will be written to file
        noteFileName: If you wish to change the name of the file, by defualt it is `note` + time and date.
        saveLocation: If you wish to change the location of the file, by default it is saved in the same directory as this script.
        
    Returns:
        True: if the file was successfully created and written to.
        False: if there was an error.
        
    Function Author: Mason Hedger"""

    fileName = ""
    now = datetime.now()

    # Check if noteFileName is anything but default value.
    # We also double check that it is a string.
    if(noteFileName != None and type(noteFileName) is str):
        fileName = noteFileName + ".txt"
    else:
        # Otherwise, use the default file name
        fileName = "note" + now.strftime("%Y%m%d_%H_%M") + ".txt"

    # Check if saveLocation is anything but default value.
    # We also double check that it is a string.
    if(saveLocation != None and type(saveLocation) is str):
        fileName = saveLocation + "/" + fileName

    # Error handling
    try:
        # create and open file
        with open(fileName, "w") as noteFile:
            noteFile.write(noteData)

        # If we successfully wrote out, return true
        return True
    except Exception as e:
        # Warn via console.
        print(f"There was an issue saving file: {fileName}!! File not saved.")
        # Display error.
        print(e)

    # By Default, return False
    return False