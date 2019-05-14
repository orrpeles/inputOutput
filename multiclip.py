#!/bin/python
# Program saves and loads pieces of text to clipboard
# reference: mcb.pynb

# Usage: python.multiclip.py save <keyword> - Saves clipboard to keyword.
#        python.multiclip.py <keyword> - Loads keyword to clipboard.
#        python.multiclip.py list - Loads all keywords to clipboard

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# elif len(sys.argv) == 2:
mcbShelf.close()

