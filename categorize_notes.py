import os

# Keywords used to decide each note's category
# TODO: Placeholder categories - group still needs to decide the final list
CATEGORIES = {
    "Category 1": ["keyword1", "keyword2"],
    "Category 2": ["keyword3", "keyword4"],
}


def categorize_notes(folder="."):
    """Sorts each saved note into a category by counting keywords.
    Writes an organization plan but does NOT move any files.

    Function Writer: Christian Landa"""
    categorized = {}

    for fileName in os.listdir(folder):
        if fileName.startswith("note") and fileName.endswith(".txt"):
            with open(os.path.join(folder, fileName), "r") as noteFile:
                text = noteFile.read().lower()

            # Pick the category with the most keyword matches
            best = "Uncategorized"
            best_score = 0
            for category, keywords in CATEGORIES.items():
                score = sum(text.count(word) for word in keywords)
                if score > best_score:
                    best, best_score = category, score

            categorized.setdefault(best, []).append(fileName)

    # Save the plan and show it
    with open("organization_plan.txt", "w") as plan:
        print("\n--=NOTES BY CATEGORY=--")
        for category, files in categorized.items():
            print(f"{category}: {', '.join(files)}")
            plan.write(f"{category}: {', '.join(files)}\n")

    return categorized 
