#!/usr/bin/python
import re
import argparse
import sys

replacements = [
    ('\r', '', 0, 0),
    (r'\\label{.*?}', '', 0, 0),
    (r'\.\.\.', '\ldots{}', 0, 0),
    (r'\\begin{quote}', r'\\begin{quotation}', 0, 0),
    (r'\\end{quote}', r'\\end{quotation}', 0, 0),
]


parser = argparse.ArgumentParser(
    description='Clean up LaTeX output from Pandoc')
parser.add_argument('files', metavar='FILE', nargs='*')
parser.add_argument('-i', '--in-place', action='store_true',
    help='edit files in place')
args = parser.parse_args()

def do_replacements(string):
    for pattern, repl, count, flags in replacements:
        string = re.sub(pattern, repl, string, count, flags)
    return string

if args.files:
    if args.in_place:
        for filename in args.files:
            f = open(filename)
            content = f.read()
            f.close()
            content = do_replacements(content)
            f = open(filename, 'w')
            f.write(content)
            f.close()
    else:
        for filename in args.files:
            sys.stdout.write(do_replacements(open(filename).read()))
elif args.in_place:
    parser.error('no input files')
else:
    sys.stdout.write(do_replacements(sys.stdin.read()))
