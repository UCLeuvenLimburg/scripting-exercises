import urllib.request
import sys

word = sys.argv[1]

with urllib.request.urlopen(f"{word}") as input:
    contents = input.read()
    print(contents)
