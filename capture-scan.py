#!/usr/bin/env python
# Name: capture-scan.py
# Author: Mark Spicer
# Purpose: Reads a packet capture and then port scans each unique host.

# Necessary modules.
import argparse         # Used to parse command line arguements.
import csv

# Parse command line arguements passed to the script.
parser = argparse.ArgumentParser(description=
    'Reads a packet capture and then port scans each unique host.')
parser.add_argument('-i, --input', dest='input_file',
    help='Capture file to parse.')
args = parser.parse_args()
