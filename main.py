# main.py
from braille_corrector import suggest_word
from braille_utils import convert_qwerty_to_braille

while True:
    user_input = input("Enter Braille QWERTY key sequence for a word (comma-separated keys, e.g., D,W,Q,D,O): ")
    if user_input.lower() == "exit":
        break
    try:
        # Split input into individual keys
        keys = [k.strip() for k in user_input.split(',') if k.strip()]
        if not keys:
            print("Error: Invalid input. Enter comma-separated key groups (e.g., D,W,Q,D,O).")
            continue

        # Group keys into letters (1-4 keys per Braille letter)
        letters = []
        i = 0
        while i < len(keys):
            current_group = [keys[i]]
            i += 1
            # Continue adding keys to the current group (up to 4 keys)
            # Stop if we encounter a key that likely starts a new letter
            while i < len(keys) and len(current_group) < 4:
                next_key = keys[i]
                # If the next key is 'D' or 'W' and the current group has 2 or more keys,
                # it's likely the start of a new letter (based on Braille patterns)
                if next_key.upper() in ['D', 'W'] and len(current_group) >= 2:
                    break
                current_group.append(next_key)
                i += 1
            letters.append(','.join(current_group))

        print("Parsed letters:", letters)
        if not letters:
            print("Error: Invalid input. Enter comma-separated key groups (e.g., D,W,Q,D,O).")
            continue
        word = convert_qwerty_to_braille(letters)
        print("Converted word:", word)
        suggestion = suggest_word(word)
        print("Suggestions:", suggestion if suggestion else "None")
    except Exception as e:
        print(f"Error: {e}")