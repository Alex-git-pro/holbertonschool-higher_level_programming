#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.
    
    Arguments:
    text -- the text to print
    
    If `text` is not a string, raises a TypeError with the message "text must be a string".
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    
    # Loop through the text and print each character
    i = 0
    while i < len(text):
        # Print the character
        print(text[i], end="")
        
        # Check if the current character is one of '.', '?', or ':'
        if text[i] in ['.', '?', ':']:
            # If so, print two new lines
            print("\n")
            # Skip any additional spaces after the punctuation mark
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
