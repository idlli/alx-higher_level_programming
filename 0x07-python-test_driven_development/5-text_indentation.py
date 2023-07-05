#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.replace('?', '.')
    text = text.replace(':', '.')
    text = text.split('.')
    print(*map(str.strip, text), sep='\n\n', end='')
