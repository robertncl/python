#!/usr/bin/env python3
import sys
import unicodedata

FIRST, LAST = ord(' '), sys.maxunicode              


def find(*query_words, first=FIRST, last=LAST):     
    query = {w.upper() for w in query_words}        
    count = 0
    for code in range(first, last + 1):
        char = chr(code)                            
        name = unicodedata.name(char, None)         
        if name and query.issubset(name.split()):   
            print(f'U+{code:04X}\t{char}\t{name}')  
            count += 1
    print(f'({count} found)')


def main(words):
    if words:
        find(*words)
    else:
        print('Please provide words to find.')


if __name__ == '__main__':
    main(sys.argv[1:])