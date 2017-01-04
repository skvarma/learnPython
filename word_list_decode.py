#!/usr/bin/env python3
"""Retirve & print words from  URL"""
from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: url of an utf-8 text document

    Returns:
        A list of strings from the document.
    """
    # with urlopen('http://sixty-north.com/c/t.txt') as story:
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)

if (__name__ == "__main__"):
    main(sys.argv[1])
