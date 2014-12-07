#!/usr/bin/env python
# Name: capture-scan.py
# Author: Mark Spicer
# Purpose: Reads a packet capture and then port scans each unique host.

# Import necessary modules.
import argparse         # Used to parse command line arguements.
import csv              # Used to parse csv files.

# Parse command line arguements passed to the script.
parser = argparse.ArgumentParser(description=
    'Reads a packet capture and then port scans each unique host.')
parser.add_argument('-i, --input', dest='input_file',
    help='Capture file to parse.')
args = parser.parse_args()

# Open captured input file.
with open(args.input_file, 'rb') as csvfile:
    capture = csv.DictReader(csvfile)
    for row in capture:
        print(row['Source'],row['Destination'])
