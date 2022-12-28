from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = [
    'ch10/alice.txt',
    'ch10/siddhartha.txt',
    'ch10/moby_dick.txt',
    'ch10/little_women.txt',
]

for filename in filenames:
    path = Path(filename)
    count_words(path)
