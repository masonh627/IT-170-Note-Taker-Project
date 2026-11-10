# Title: Note Building Project.
# Description: Tool that helps the user take and store notes.
# Authors: Manuel G, Carlos G, Mason H, Christian L, Elijah M, Jacobi T.

# This will be our main python script.

# Needed for naming the notes files
from datetime import datetime

def browse_notes(filename='notes.txt'):
    # This function was created by Christian Landa
    """ Retrieves and displays all saved notes so the user can select and read a previous note. """
    try:
        with open(filename,'r') as file:
            data = []
            lines = file.readlines()

        # 1. Parse the lines into note items
        # Assume each note is separated by blanks or delimiters
        current_note = []
        for line in lines:
            # Strip whitespace from the line
            clean_line = line.strip()

            # If we encounter a delimiter or blank
            if clean_line == '---' or (not clean_line and current_note):
                if current_note:
                    items = {
                        # First line acts as the title
                        "title": current_note[0], 
                        "body": "\n".join(current_note)
                    }
                    data.append(items)
                    current_note = []
            elif clean_line and clean_line != '---':
                current_note.append(clean_line)

        # Catch the last note if the file doesn't end with a delimiter
        if current_note:
            items = {
                "title": current_note[0],
                "body": "\n".join(current_note)
            }
            data.append(items)
            """Version that excludes title from the body
            items = {
                "title": current_note[0],
                "body": "\n".join(current_note[1:])
            }
            data.append(items)"""

        # 2. Check if we found any notes
        if not data:
            print("There are no notes found in the file.")
            return data

        #3. Display notes to user
        print("\n--=SAVED NOTES=--")
        for index, items in enumerate(data, start=1):
            print(f"[{index}] {items['title']}")
        print ("[0] Exit")

        # 4. User selection
        while True:
            try:
                choice = int(input("\nEnter the number of the note you want to read: "))
                if choice == 0:
                    print("Exiting.")
                    break
                elif 1 <= choice <= len(data):
                    selected_note = data[choice -1 ]
                    print(f"\n-== READING NOTE: {selected_note['title']} ==-")
                    print(selected_note['body'])
                    print("-" * 30)
                    break
                else:
                    print(f" Invalid choice. Please try again and select between 1 and {len(data)}.")
            except ValueError:
                print("Please enter a valid number.")

        return data

    except FileNotFoundError:
        print(f" Error: The file '{filename}' was not found.")
        return []


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