Braille Autocorrect and Suggestion System

    


 Table of Contents

*Overview

*Built Using

*Folder Structure

*Usage Documentation

*Get Started

 *Native

*Tests

*License

 Overview 
This project is a Python-based Braille Autocorrect and Suggestion System designed for Thinkerbell Labs. It allows visually impaired users to type in Braille using a QWERTY keyboard, where the keys D, W, Q, K, O, P represent Braille dots 1–6. The system converts these key sequences into English words, suggests corrections for typos, and supports Braille contractions like "the", "th", and "ing". It also includes a learning mechanism to improve suggestions over time by prioritizing frequently used words.

The pipeline is simple but effective:

*Input: Users enter comma-separated key sequences (e.g., D,W,O,D,O for "he").
*Conversion: The system converts key sequences to Braille dots and then to English letters or    contractions.
*Autocorrect: If the word isn’t in the dictionary (e.g., "hellz"), it suggests the closest match (e.g., "hello").
*Output: Displays the converted word and any suggestions.

This project aims to make Braille typing more accessible by providing real-time error correction and suggestions, enhancing the user experience for visually impaired individuals.


 Built Using 

![6124995](https://github.com/user-attachments/assets/08555600-ed24-46d8-8632-db4b63bd8f20)

unittest

    
![210414](https://github.com/user-attachments/assets/4d2b7185-b862-4a9a-8654-79ad0faecde3)

python-Levenshtein



 Folder Structure 
 
Here’s the folder structure of the Braille Autocorrect project:

    BrailleAutoCorrectProject/
    ├── braille_autocorrect/
    │   ├── main.py             # Main script for user interaction
    │   ├── braille_utils.py    # Braille conversion logic
    │   ├── braille_corrector.py # Autocorrect and suggestion logic
    │   ├── test_corrector.py   # Unit tests for the system
    │   ├── dictionary.txt      # Dictionary file for word lookup
    │   ├── learned_suggestions.txt # Tracks suggestion usage for learning
    │   ├── README.md           # Project documentation
    │   └── ...                 # Additional files
    ├── venv/                   # Virtual environment
    └── ...                     # Other project files

This structure keeps all the core functionality in the braille_autocorrect/ directory, making it easy to manage and run.
 Usage Documentation 
The project is a command-line application. To use it:

 * Run main.py to start the program.
 * Enter a comma-separated key sequence (e.g., D,W,O,D,O) representing Braille letters.
 * The program will output the parsed letters, the converted word, and any suggestions if the word       isn’t in the dictionary.
 *Type exit to quit.
Detailed examples are provided in the Get Started section below.


 Get Started 
 
 Native 
 
Navigate to the Project Directory  

    cd /Users/vinaysproperty/BrailleAutoCorrectProject/braille_autocorrect

Activate the Virtual Environment
If not already activated:  

    source /Users/vinaysproperty/BrailleAutoCorrectProject/venv/bin/activate

Install DependenciesThe project uses python-Levenshtein for autocorrect:  

    pip3 install python-Levenshtein

Run the Application  
    
    python3 main.py


* Follow the prompt to enter a key sequence.
* Example: Enter D,W,O,D,O,D,W,Q,D,W,Q,D,Q,O to type "hello".

Run Tests (Optional)
To verify the system works:  

    python3 test_corrector.py

 Tests 
The project includes unit tests to ensure reliability.
Run All TestsFrom the braille_autocorrect/ directory:  

    python3 test_corrector.py

This runs 8 tests covering conversion, autocorrect, contractions, and error handling.
Expected output:

    ........
    ----------------------------------------------------------------------
    Ran 8 tests in 0.001s
    
    OK

Features Implemented:

Braille-to-English conversion using QWERTY keys.

Autocorrect with Levenshtein distance.

Support for contractions (e.g., W,O → "the").

Learning mechanism to prioritize frequent suggestions.


 License 
This project is licensed under the MIT License. See the LICENSE file for more information (if a repository is created).

    © 2025 Vinay S.
