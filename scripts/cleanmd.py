#!/usr/bin/python
import re
import argparse
import sys

replacements = [
    (r'\r', '', 0, 0),
    (r'\n\\\n', '', 0, 0),
    (r'</?span.*?>', '', 0, 0),
    (r'</?div.*?>', '', 0, 0),
    (r'\. \. \.', '...', 0, 0),
    ('\x04', '', 0, 0),
    ('\x05', '', 0, 0),
]

parser = argparse.ArgumentParser(
    description='Clean up Markdown output from Pandoc')
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
