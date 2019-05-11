#!/usr/bin/env python3
"""Preliminary exercises for Part IIA Project GF2."""
import sys
from mynames import MyNames


def open_file(path):
    """Open and return the file specified by path."""
    try:
        fo = open(path, "r")
    except IOError:
        print("ERROR: Cannot open file; check file exists")
        sys.exit()
    else:
        return fo
        fo.close()


def get_next_character(input_file):
    """Read and return the next character in input_file."""
    ch = input_file.read(1)
    return ch


def get_next_non_whitespace_character(input_file):
    """Seek and return the next non-whitespace character in input_file."""
    ch = input_file.read(1)
    while ch.isspace():
        ch = input_file.read(1)
    return ch


def get_next_number(input_file):
    """Seek the next number in input_file.
    Return the number (or None) and the next non-numeric character.
    """
    ch = input_file.read(1)
    while not(ch.isdigit() or ch == ""):
        ch = input_file.read(1)
    if ch == "":
        ans = [None, ""]
    else:
        num = ""
        while ch.isdigit():
            num = num + ch
            ch = input_file.read(1)
        ans = [num, ch]
    return ans


def get_next_name(input_file):
    """Seek the next name string in input_file.
    Return the name string (or None) and the next non-alphanumeric character.
    """
    ch = input_file.read(1)
    while not(ch.isalpha() or ch == ""):
        ch = input_file.read(1)
    if ch == "":
        ans = [None, ""]
    else:
        nam = ""
        while ch.isalnum():
            nam = nam + ch
            ch = input_file.read(1)
        ans = [nam, ch]
    return ans


def main():
    """Preliminary exercises for Part IIA Project GF2."""

    # Check command line arguments
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("Error! One command line argument is required.")
        sys.exit()

    else:
        path = arguments[0]

        print("\nNow opening file " + path)
        # Print the path provided and try to open the file for reading
        fo = open_file(path)

        print("\nNow reading file " + path)
        # Print out all the characters in the file, until the end of file
        eof = False
        while not(eof):
            c = get_next_character(fo)
            print(c, end="")
            if c == "":
                eof = True

        print("\nNow skipping spaces...")
        # Print out all the characters in the file, without spaces
        fo.seek(0, 0)
        eof = False
        while not(eof):
            c = get_next_non_whitespace_character(fo)
            print(c, end="")
            if c == "":
                eof = True

        print("\nNow reading numbers...")
        # Print out all the numbers in the file
        fo.seek(0, 0)
        eof = False
        while not(eof):
            num = get_next_number(fo)
            if num[0] is not None:
                print(num[0], end=",")
            if num[1] == "":
                eof = True

        print("\nNow reading names...")
        # Print out all the names in the file
        fo.seek(0, 0)
        eof = False
        while not(eof):
            nam = get_next_name(fo)
            if nam[0] is not None:
                print(nam[0], end=",")
            if nam[1] == "":
                eof = True

        print("\nNow censoring bad names...")
        # Print out only the good names in the file
        fo.seek(0, 0)
        eof = False
        name = MyNames()
        bad_name_ids = [name.lookup("Terrible"), name.lookup("Horrid"),
                        name.lookup("Ghastly"), name.lookup("Awful")]
        while not(eof):
            nam = get_next_name(fo)
            if nam[0] is not None:
                id = name.lookup(nam[0])
                if bad_name_ids.count(id) == 0:
                    print(name.get_string(id), end=",")
            if nam[1] == "":
                eof = True


if __name__ == "__main__":
    main()
