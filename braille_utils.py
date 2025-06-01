# braille_utils.py
def convert_qwerty_to_braille(key_sequence):
    # Map QWERTY keys to Braille dots
    key_to_dot = {'D': 1, 'W': 2, 'Q': 3, 'K': 4, 'O': 5, 'P': 6}
    # Braille dot patterns for English alphabet (lowercase)
    braille_to_char = {
        (1,): 'a',           # D
        (1, 2): 'b',         # D,W
        (1, 4): 'c',         # D,K
        (1, 4, 5): 'd',      # D,K,O
        (1, 5): 'e',         # D,O
        (1, 2, 4): 'f',      # D,W,K
        (1, 2, 4, 5): 'g',   # D,W,K,O
        (1, 2, 5): 'h',      # D,W,O
        (2, 4): 'i',         # W,K
        (2, 4, 5): 'j',      # W,K,O
        (1, 3): 'k',         # D,Q
        (1, 2, 3): 'l',      # D,W,Q
        (1, 3, 4): 'm',      # D,Q,K
        (1, 3, 4, 5): 'n',   # D,Q,K,O
        (1, 3, 5): 'o',      # D,Q,O
        (1, 2, 3, 4): 'p',   # D,W,Q,K
        (1, 2, 3, 4, 5): 'q',# D,W,Q,K,O
        (1, 2, 3, 5): 'r',   # D,W,Q,O
        (2, 3, 4): 's',      # W,Q,K
        (2, 3, 4, 5): 't',   # W,Q,K,O
        (1, 3, 6): 'u',      # D,Q,P
        (1, 2, 3, 6): 'v',   # D,W,Q,P
        (2, 4, 5, 6): 'w',   # W,K,O,P
        (1, 3, 4, 6): 'x',   # D,Q,K,P
        (1, 3, 4, 5, 6): 'y',# D,Q,K,O,P
        (1, 3, 5, 6): 'z'    # D,Q,O,P
    }
    # Braille contractions (common ones)
    braille_contractions = {
        (2, 3, 4, 6): 'th',  # W,Q,K,P
        (2, 3, 5, 6): 'ing', # W,Q,O,P
        (2, 5): 'the'        # W,O
    }
    
    result = []
    for keys in key_sequence:
        key_list = [k.strip().upper() for k in keys.split(',')]
        try:
            dots = tuple(sorted([key_to_dot[key] for key in key_list if key in key_to_dot]))
            # Check for contractions first
            if dots in braille_contractions:
                char = braille_contractions[dots]
            else:
                char = braille_to_char.get(dots, '?')
            result.append(char)
        except KeyError:
            return "Error: Invalid key in sequence"
    return ''.join(result)