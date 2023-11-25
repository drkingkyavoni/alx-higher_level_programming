#!/usr/bin/python3
"""
    Module contains text_indentation
    Returns: None
    Tests contained in tests/5-text_indentation.txt
"""


def text_indentation(text: str):
    """
        Function prints new line for delimeters "?", ".", ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for elem in ['.', '?', ':']:
        text = text.replace(elem, elem + "|\n|")
    print("\n".join(elem.strip() for elem in text.split("|")), end="")
