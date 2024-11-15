import random
import re

"""
Function: count_syllables
- Estimates number of syllables in a word using vowel groups.
- Cases accounted for: words ending with silent 'e' and 'le'.
"""
def count_syllables(word):
    word = word.lower()
    # Count vowel groups using regex:
    syllable_count = len(re.findall(r'[aeiouy]+', word))
    # Debugging output:
    print(f"Word: {word}, Syllable Count (before adjustments): {syllable_count}")
    # Handle silent 'e', 'es', 'ed', 'ion' at the end of the word:
    if (word.endswith('e') or 
        (word.endswith('es') and len(word) > 2 and len(word) < 8) or 
        word.endswith('ed') or word.endswith('ion')) and syllable_count > 1:
        syllable_count -= 1
    # Handle 'le' at the end of the word, or words like 'photo', 'cry':
    if word.endswith('le') and len(word) > 2 and word[-3] not in "aeiouy":
        syllable_count += 1
    # Adjust for vowel pairs:
    syllable_count -= len(re.findall(r'(ea|eo|ou|oo|ei|eu|hua|oy|ey|ay)(?![aeiouy])', word))
    # Adjust for adjacent vowels often split into separate syllables:
    syllable_count += len(re.findall(r'(ia|eo|oe|ua|io)', word))
    # Treat 'ea' in the middle as two syllables:
    if re.search(r'ea', word) and len(re.findall(r'[aeiouy]+', word)) == 1 and word not in ["sea", "pea", "lea"]:
        syllable_count += 1  # Add one more syllable for "ea" in words like "weary"
    # Ensure at least 1 syllable per word:
    return max(1, syllable_count)

"""
Function: format_haiku_line
- Forms a lines with their respective number of syllables.
- Adds words from the given list until the syllable count for each line (5, 7, & 5) meets the target value.
"""
def format_haiku_line(words, target_syllables):
    line = []
    syllable_count = 0
    # Debugging output:
    print(f"Starting line with target {target_syllables} syllables.")
    for i, word in enumerate(words):
        syllables_in_word = count_syllables(word)
        # Debugging output:
        print(f"Word: {word}, Syllables in word: {syllables_in_word}, Current syllable count: {syllable_count}")
        if syllable_count + syllables_in_word <= target_syllables:
            line.append(word)
            syllable_count += syllables_in_word
        if syllable_count == target_syllables:
            print(f"Line complete: {' '.join(line)}")
            break
    # Return the line and the remaining words:
    remaining_words = words[len(line):]
    # Debugging output:
    print(f"Remaining words after forming line: {remaining_words}")
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