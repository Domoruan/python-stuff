#!/usr/bin/env python3

import sys

def text_to_hex(text):
    """
    Convert a given text string to its hexadecimal representation.

    Args:
        text (str): Input string to convert.

    Returns:
        str: Hexadecimal representation of the input text.
    """
    return text.encode('utf-8').hex()

def main():
    if len(sys.argv) < 2:
        print("Usage: text_to_hex.py <text>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])  # Combine all command-line arguments as input text
    hex_result = text_to_hex(text)
    print(f"Hexadecimal representation: {hex_result}")

if __name__ == "__main__":
    main()
