"""
pip install cmudict
pip install nltk
/Applications/Python\ 3.11/Install\ Certificates.command
"""

import random
import cmudict
import nltk
from nltk.corpus import cmudict
import logging
from nltk import download

# Suppress NLTK's download messages:
logging.getLogger('nltk').setLevel(logging.CRITICAL)
# Disable tqdm progress bar for downloads:
nltk.download('cmudict', quiet=True)
# Load the CMU Pronouncing Dictionary:
d = cmudict.dict()
print(d.get('cruel'))


"""
Function: count_syllables
- Estimates number of syllables in a word using vowel groups.
- Cases accounted for: words ending with silent 'e' and 'le'.
"""
def count_syllables(word):
    word = word.lower()
    # Try to find the word in CMUdict dictionary:
    if word in d:
        # Get all possible pronunciations and select the one with the fewest syllables:
        syllable_count = min([len([y for y in x if y[-1].isdigit()]) for x in d[word]])
        # Error checking print statement for debugging
        #print(f"Word: {word}, Syllables: {syllable_count}")
        return syllable_count
    else:
        # If word is not in CMUdict, return 1 syllable as a fallback:
        #print(f"Word: {word}, Syllables: 1 (fallback)")  # For words not found in CMUdict
        return 1

"""
Function: format_haiku_line
- Forms a lines with their respective number of syllables.
- Adds words from the given list until the syllable count for each line (5, 7, & 5) meets the target value.
"""
def format_haiku_line(words, target_syllables):
    line = []
    syllable_count = 0
    for i, word in enumerate(words):
        syllables_in_word = count_syllables(word)
        if syllable_count + syllables_in_word <= target_syllables:
            line.append(word)
            syllable_count += syllables_in_word
        if syllable_count == target_syllables:
            break
    print(f"Formed line: {' '.join(line)} | Syllable count: {syllable_count}")
    remaining_words = words[len(line):]
    return " ".join(line), remaining_words

"""
Function: generate_haiku
- Temporary function: Generates a haiku using a random line from the test .txt file.
- Finally prints the haiku in the formatted 5-7-5 structure.
"""
def generate_haiku(filename):
    # Read all lines from the file:
    with open(filename, 'r') as f:
        lines = f.readlines()
    # Select a random line and split into words:
    selected_line = random.choice(lines).strip()
    words = selected_line.split()
    # Generate 5-7-5 haiku:
    haiku = []
    for target_syllables in [5, 7, 5]:
        line, words = format_haiku_line(words, target_syllables)
        haiku.append(line)
    # Print the haiku:
    return "\n".join(haiku)

# Usage:
filename = 'backend/testhaikus.txt'
print(generate_haiku(filename)) # Prints to terminal.