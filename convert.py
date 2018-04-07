#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(
    description='This Script Encode and Decode ASCII Text Images'
)

parser.add_argument(
    '--encode',
    help='Encode the ASCII Image from a text file',
)

parser.add_argument(
    '--decode',
    help='Decode the ASCII Image from a text file',
)

args = parser.parse_args()


def encode(line):
    """
    INPUT:  A line of ASCII String.
    OUTPUT: A List of Run-Length Encoded of the input string.
    """
    if not line:
        return [""]

    else:
        last_char = line[0]
        length = len(line)
        i = 1
        while i < length and last_char == line[i]:
            i += 1
        return [str(i), last_char] + encode(line[i:])


def decode(parsed_string):
    """
    INPUT:  A List of List parsed from encoded string
    OUTPUT: A String of Decoded line
    """
    decoded = ""
    for item in parsed_string:
        try:
            decoded += item[0] * item[1]
        except IndexError:
            pass
    return decoded


def flatten(encoded_list):
    """
    INPUT:  A list of encoded ASCII String
    OUPUT:  A String of encoded ASCII String
    """
    return "".join(encoded_list)


def parse(string):
    """
    This function parses the encoded string for the decoding phase.
    This is especially userful when a character shows up
    more than nine times in a row.

    INPUT:  An Encoded String
    OUTPUT: A List of List // Parsed Encoded String
    """
    if not string or len(string) == 1:
        return [""]

    if string[1].isdigit():
        return [[int(string[:2]), string[2]]] + parse(string[3:])
    else:
        return [[int(string[0]), string[1]]] + parse(string[2:])


def main():
    # ENCODING
    if args.encode:
        with open(sys.argv[2], 'r') as f:
            with open("encoded_data.txt", 'w+') as o:
                for line in f:
                    encoded_string = flatten((encode(line)))
                    o.write(encoded_string)
    # DECODING
    else:
        with open(sys.argv[2], 'r') as f:
            with open("decoded_data.txt", 'w+') as o:
                for line in f:
                    parsed_string = parse(line)
                    o.write(decode(parsed_string))


if __name__ == '__main__':
    main()
