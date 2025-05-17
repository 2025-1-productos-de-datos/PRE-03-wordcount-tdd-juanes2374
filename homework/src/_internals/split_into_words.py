import re

def split_into_words(lines):
    words = []
    for line in lines:
        # Quita puntuación y separa en palabras
        line_words = re.findall(r'\b\w+\b', line)
        words.extend(line_words)
    return words
