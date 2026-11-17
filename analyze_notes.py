import os
from collections import Counter


def analyze_notes(folder="."):
    """Shows basic stats about the saved notes.

    Function Author: Christian Landa"""
    word_counts = {}
    all_words = Counter()

    for fileName in os.listdir(folder):
        if fileName.startswith("note") and fileName.endswith(".txt"):
            with open(os.path.join(folder, fileName), "r") as noteFile:
                words = noteFile.read().lower().split()
            word_counts[fileName] = len(words)
            all_words.update(words)

    if not word_counts:
        print("There are no notes to analyze.")
        return {}

    total = sum(word_counts.values())
    print("\n--=NOTES ANALYSIS=--")
    print(f"Total notes: {len(word_counts)}")
    print(f"Total words: {total}")
    print(f"Average words per note: {total / len(word_counts):.1f}")
    print(f"Longest note: {max(word_counts, key=word_counts.get)}")
    print(f"Most common words: {all_words.most_common(5)}")

    return word_counts
