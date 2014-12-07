#!/usr/bin/env python
# Name: capture-scan.py
# Author: Mark Spicer
# Purpose: Reads a packet capture and then port scans each unique host.

# Import necessary modules.
import argparse         # Used to parse command line arguements.
import csv              # Used to parse csv files.
from IPy import IP
from scan import *

"""
Functions
"""
def check_unique(ip, unique_ips):
    if ip in unique_ips:
        next
    else:
        if check_valid(ip):
            unique_ips.append(ip)
        else:
            print "Skipping %s" % ip

def check_valid(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

"""
Main Program
"""
# Parse command line arguements passed to the script.
parser = argparse.ArgumentParser(description='Reads a packet capture and \
                                then port scans each unique host.')
parser.add_argument('-i, --input', dest='input_file',
                    help='Capture file to parse.')
args = parser.parse_args()

# A list used to store unique IP addresses.
unique_ips = []

# Open captured input file and check which IP addresses are unique.
with open(args.input_file, 'rb') as csvfile:
    capture = csv.DictReader(csvfile)
    for row in capture:
        check_unique(row['Source'], unique_ips)
        check_unique(row['Destination'], unique_ips)

# Define variables for the creation of threads.
count = 0
threads = []

# Iterate through each unique IP address.
for ip in unique_ips:
    try:
        t = scan(count, "Thread-" + str(count), ip)
        threads.append(t)
        t.start()
        count += 1
    except Exception,e:
        print "\t%s" %e

# Print out data generated by the nmap scans.
for t in threads:
    # Wait for the thread to finish before accessing data.
    t.join()
    nm = t.results()

    # Iterate through each host and print out info.
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())

            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)

                lport = nm[host][proto].keys()
                lport.sort()
                for port in lport:
                    print('port : %s\tstate : %s' %
                        (port, nm[host][proto][port]['state']))
