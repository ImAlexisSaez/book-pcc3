from pathlib import Path


def count_a_word(path, word):
    """Count the approximate number of occurrences of a word in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.lower()        
        num_words = words.count(word)
        print(f"The file {path} has about {num_words} '{word}'.")


filenames = [
    'ch10/alice.txt',
    'ch10/siddhartha.txt',
    'ch10/moby_dick.txt',
    'ch10/little_women.txt',
]

word = 'the '

for filename in filenames:
    path = Path(filename)
    count_a_word(path, word)
