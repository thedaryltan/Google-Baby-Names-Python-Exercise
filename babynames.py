#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


import argparse
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
    try:
        with open(filename, 'r') as f:
            file_text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError("The file you provided does not exist.")
    except UnicodeDecodeError:
        print("The file you provided is not a valid HTML file.")
        exit(1)
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
    return "\n".join(text_to_print)


def get_user_filename():
    """
    this function handles the user input for the filename and the
    --summaryfile flag
    returns args.filename as a string and args.summaryfile as a boolean
    """
    parser = argparse.ArgumentParser(
        prog='calculator',
        description='runs mathematical operations on two numbers')
    parser.add_argument('filename', type=str, metavar='filename',
                        help="provide the filename of the file you wish to "
                             "parse")

    parser.add_argument('--summaryfile', action='store_true',
                        required=False, help="use this flag if want the "
                                             "results to be written into a "
                                             "summary file")
    args = parser.parse_args()
    if args.filename[-5::].lower() != ".html":
        raise ValueError("The filename you provide must end in .html")
    return args.filename, args.summaryfile


def write_to_file(filename, new_file_text):
    """
    receives the original filename and the new_file_text that should be
    written into the new file
    creates a new file at the same location as the original file with
    .summary appended to the name and the summarised text as content
    """
    new_file_name = filename + ".summary"
    with open(new_file_name, "w") as f:
        f.write(new_file_text)


def display_result(new_file_text):
    """
    receives the new_file_text string which is the summary of the HTML file
    prints it for the user
    """
    print(new_file_text)


def _run_extract_names():
    """
    called by the main function to run the functions
    calls on get_user_filename for userinput
    calls on extract_names to parse the HTML file and format the content
    calls on write_to_file to create the new file with the new content
    calls on display_result to print the results to the user
    """
    filename, summary_file = get_user_filename()
    new_file_text = extract_names(filename)
    if summary_file is True:
        write_to_file(filename, new_file_text)
    display_result(new_file_text)


def main():
    _run_extract_names()


if __name__ == '__main__':
    main()
