#!/usr/bin/python
import re
import argparse
import sys
import csv

parser = argparse.ArgumentParser(
    description='Substitute based on CSV-file')
parser.add_argument('files', metavar='FILE', nargs='*')
parser.add_argument('-i', '--in-place', action='store_true',
    help='edit files in place')
parser.add_argument('-c', '--csv-file', metavar='CSV', type=file,
    help='specify CSV file other than "subs.csv"')
args = parser.parse_args()

def do_replacements(subs, string):
    for sublist in subs:
        repl = sublist[0]
        patterns = sublist[1:]
        for pattern in patterns:
            string = re.sub(pattern, repl, string)
    return string

if not args.csv_file:
    args.csv_file = open('subs.csv')

subs = [x for x in csv.reader(args.csv_file)]

if args.files:
    if args.in_place:
        for filename in args.files:
            f = open(filename)
            content = f.read()
            f.close()
            content = do_replacements(subs, content)
            f = open(filename, 'w')
            f.write(content)
            f.close()
    else:
        for filename in args.files:
            sys.stdout.write(do_replacements(subs, open(filename).read()))
elif args.in_place:
    parser.error('no input files')
else:
    sys.stdout.write(do_replacements(subs, sys.stdin.read()))
