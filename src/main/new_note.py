def new_note():
    # Function by Carlos G
    """Collects a note name and the note text one line at a time.
    Stops when the user types END. Returns the note as one string,
    or an empty string if nothing was entered."""
    name = input("Enter note name: ").strip()
    print("Enter your note below. When finished, type END")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip():          # skip blank lines, see below
            lines.append(line)

    if not name or not lines:
        print("Nothing to save.")
        return ""

    return name + "\n" + "\n".join(lines) + "\n---\n"


