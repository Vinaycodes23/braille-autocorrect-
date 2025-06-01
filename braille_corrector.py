# braille_corrector.py
from Levenshtein import distance
import os

# Path to dictionary file
DICTIONARY_FILE = "dictionary.txt"
# Path to store learned suggestions (for bonus feature)
LEARNED_SUGGESTIONS_FILE = "learned_suggestions.txt"

# Load dictionary from file
def load_dictionary():
    try:
        with open(DICTIONARY_FILE, 'r') as f:
            return [word.strip().lower() for word in f.readlines() if word.strip()]
    except FileNotFoundError:
        print(f"Error: {DICTIONARY_FILE} not found. Using default dictionary.")
        return ["hello", "test", "braille", "something", "world", "code"]

# Load learned suggestions (word -> frequency of selection)
def load_learned_suggestions():
    learned = {}
    if os.path.exists(LEARNED_SUGGESTIONS_FILE):
        with open(LEARNED_SUGGESTIONS_FILE, 'r') as f:
            for line in f:
                word, freq = line.strip().split(':')
                learned[word] = int(freq)
    return learned

# Save learned suggestions
def save_learned_suggestions(learned):
    with open(LEARNED_SUGGESTIONS_FILE, 'w') as f:
        for word, freq in learned.items():
            f.write(f"{word}:{freq}\n")

def suggest_word(input_text):
    dictionary = load_dictionary()
    learned = load_learned_suggestions()
    
    if input_text == "Error: Invalid key in sequence":
        return ["Invalid input; try valid keys: D, W, Q, K, O, P"]
    
    if input_text in dictionary:
        return None
    
    # Calculate Levenshtein distance for each word in dictionary
    suggestions = []
    for word in dictionary:
        dist = distance(input_text, word)
        if dist <= 2:  # Threshold for "close" match
            # Prioritize words that were frequently selected (learning mechanism)
            freq = learned.get(word, 0)
            suggestions.append((dist, -freq, word))  # Sort by distance, then frequency (descending)
    
    if not suggestions:
        return None
    
    # Sort suggestions by distance (ascending) and frequency (descending)
    suggestions.sort()
    suggested_words = [word for _, _, word in suggestions]
    
    # Update learned suggestions (for demonstration, assume user selects the first suggestion)
    if suggested_words:
        first_suggestion = suggested_words[0]
        learned[first_suggestion] = learned.get(first_suggestion, 0) + 1
        save_learned_suggestions(learned)
    
    return suggested_words