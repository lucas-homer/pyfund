"""Retrieve and print words from a URL.
/Users/lucashomer/pyfund/words.py
Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words():
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.abs

    Returns:
        A list of strings containing the words from 
        the document.
    
    """
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.abs

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main():
    """Print each word from a text document from a URL.

    Args: 
        url: The URL of a UTF-8 text document. 
    """
    words = fetch_words()
    print_items(words)


if __name__ == '__main__':
    main()