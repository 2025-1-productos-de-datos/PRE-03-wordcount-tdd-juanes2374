import sys
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.count_words import count_words
from homework.src._internals.write_word_counts import write_word_counts

def main():
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    lines = read_all_lines(input_folder)
    lines = preprocess_lines(lines)
    words = split_into_words(lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)

if __name__ == "__main__":
    main()
