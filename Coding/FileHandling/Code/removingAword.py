# Removing a word from an existing file.
import re
import re

def split_with_delimiters(text, delimiters):
    """
    Splits the text by multiple delimiters but keeps the delimiters in the result.
    
    :param text: The input string
    :param delimiters: A regex pattern string for delimiters (inside a capturing group)
    :return: List of tokens including delimiters
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    if not isinstance(delimiters, str):
        raise TypeError("Delimiters must be a regex pattern string.")

    # re.split with capturing group keeps the delimiters
    return [token for token in re.split(f"({delimiters})", text) if token != ""]


fileName = input('Enter any file name: ')
with open("FileHandling/DataFiles/"+fileName, 'r') as fo:
    content = fo.read()
    deli = r"[;,|.?!@#$ ]"
    words = split_with_delimiters(content, deli)
    
with open("FileHandling/DataFiles/"+fileName, 'w') as fo:
    
    rw = input('Enter word to remove all occurrances from the file: ')
    for w in words:
        if w != rw:
            fo.write(w)
            