import json
import logging
from nltk.corpus import cmudict
from nltk import download

# Suppress NLTK's download messages
logging.getLogger('nltk').setLevel(logging.CRITICAL)

# Download CMU Pronouncing Dictionary
download('cmudict', quiet=True)
d = cmudict.dict()

def count_syllables(word):
    """
    Estimates number of syllables in a word using CMU Pronouncing Dictionary.
    """
    word = word.lower()
    if word in d:
        # Return the minimum syllable count across pronunciations
        return min([len([y for y in x if y[-1].isdigit()]) for x in d[word]])
    else:
        # Fallback for words not found
        return 1

def is_valid_haiku(haiku):
    """
    Validates if the given haiku follows the 5-7-5 syllable structure.
    """
    lines = haiku.split('. ')  # Split the haiku into lines (adjust based on your format)
    if len(lines) != 3:
        return False

    # check if haiku syllables equals 5-7-5
    target_syllables = [5, 7, 5]
    syllable_counts = [sum(count_syllables(word) for word in line.split()) for line in lines]
    return syllable_counts == target_syllables

def convert_haikus_to_gpt_jsonl(input_file, output_file):
    """
    Converts the haiku dataset to the JSONL format for fine-tuning GPT models,
    and enforcing only valid 5-7-5 haikus are included.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove leading/trailing whitespace and skip empty lines
            line = line.strip()
            if not line:
                continue
            
            # First word in each line is the theme; split the line into the theme and haiku
            parts = line.split(" ", 1)
            if len(parts) != 2:
                print(f"Skipping malformed line: {line}")
                continue
            theme, haiku = parts
            
            # Validate the 5-7-5 syllable structure
            if not is_valid_haiku(haiku):
                print(f"Skipping invalid haiku (not 5-7-5): {haiku}")
                continue
            
            # Create the JSON structure
            data = {
                "messages": [
                    {"role": "system", "content": "Marv is a 5-7-5 syllable structure haiku generator."},
                    {"role": "user", "content": theme},
                    {"role": "assistant", "content": haiku}
                ]
            }
            
            # Write to the JSONL file
            outfile.write(json.dumps(data, ensure_ascii=False) + '\n')

input_file = 'ml/HaikuRawData.txt'
output_file = 'ml/formattedData.jsonl' 
convert_haikus_to_gpt_jsonl(input_file, output_file)

