#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list
    starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    print the year at the top, then on each new line
    print the names and rank in alphabetical order
    """
    with open(filename, 'r') as f:
        file_text = f.read()
    year_match = re.search(r'Popularity\sin\s(\d{4})', file_text)
    names_match = re.findall(r"<td>(\d+)</td><td>(\w+)"
                             r"</td><td>(\w+)</td>",
                             file_text)
    text_to_print = [year_match.group(1)]
    ranked_name_dict = {}
    for matches in names_match:
        (name_rank, boy_name, girl_name) = matches
        if boy_name not in ranked_name_dict:
            ranked_name_dict[boy_name] = name_rank
        if girl_name not in ranked_name_dict:
            ranked_name_dict[girl_name] = name_rank
    for name in sorted(ranked_name_dict):
        text_to_print.append(name + ' ' + ranked_name_dict[name])
    print("\n".join(text_to_print))
    return

def get_user_filename():
    filename = input("Key in the filepath of the HTML file you wish to use: ")
    return filename

def _run_extract_names():
    filename = get_user_filename()
    extract_names(filename)


def main():
    _run_extract_names()


    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    # args = sys.argv[1:]
    #
    # if not args:
    #     print('usage: [--summaryfile] file [file ...]')
    #     sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    # summary = False
    # if args[0] == '--summaryfile':
    #     summary = True
    #     del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file


if __name__ == '__main__':
    main()
