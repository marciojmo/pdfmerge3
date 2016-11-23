#!/usr/bin/env python
"""
Merge pdf files into a single file.

EXAMPLES
    pdfmerge3 -o output.pdf
        Merges all pdf files from the current folder in lexicographic order and put the result in output.pdf

    pdfmerge3 -o output.pdf file1.pdf file2.pdf file3.pdf
        Merges file1.pdf, file2.pdf, file3.pdf (in this order) and put the result in output.pdf
"""

import os
import argparse
from PyPDF2 import PdfFileMerger


def merge(output_file="output.pdf", files_to_merge=None):
    """
    Merge pdf files into a single file.
    :param output_file: The result file.
    :param files_to_merge: The list of files to merge. If empty, all pdf files in the current directory will be
    used and merged in lexicographic order.
    """
    if not files_to_merge:
        # Load all pdf files from the current directory
        files_to_merge = sorted([x for x in os.listdir() if x.endswith(".pdf")])

    if not output_file.endswith(".pdf"):
        output_file += ".pdf"

    # Simple error checking...
    # Check if there is at least two files to merge
    if len(files_to_merge) < 2:
        print("Error: At least two pdf files are required to merge.")
        return

    # Check if the files to merge exists and if they are pdf files
    errors = []
    for f in files_to_merge:
        if not os.path.isfile(f):
            errors.append("File {0} doesn't exist.".format(f))
    if len(errors) > 0:
        print("Error: ")
        [print("    " + x) for x in errors]
        return

    # Check if the final filename conflicts with existing files
    if output_file in os.listdir():
        print("Output filename {0} conflicts with existing files".format(output_file))
        return

    # Merging files
    merger = PdfFileMerger()
    print("Merging files...")
    for f in files_to_merge:
        merger.append(open(f, 'rb'))
    with open(output_file, 'wb') as fout:
        merger.write(fout)
    print("DONE!")


def parse_args():
    """ Arguments parser """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-o", "--output", metavar="output_file")
    parser.add_argument("files_to_merge", nargs='*', metavar="files_to_merge")
    return parser.parse_args()


def main():
    """ Command line entry point """
    args = parse_args()
    if args.output:
        merge(args.output, args.files_to_merge or None)
    else:
        merge(files_to_merge=args.files_to_merge or None)
