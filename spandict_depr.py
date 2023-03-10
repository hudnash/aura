#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup

def main(argv):
    response = requests.get("http://www.spanishdict.com/translate/" + argv[0])
    soup = BeautifulSoup(response.content, "html.parser")

    for i, tag in enumerate(soup.select(".dictionary-neodict-translation-translation")):
        if i != 0:
            sys.stdout.write(", ")
        sys.stdout.write(tag.get_text())
    sys.stdout.write("\n")

if __name__ == "__main__":
    main(sys.argv[1:])