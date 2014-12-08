#!/usr/bin/env python
# Name: scan.py
# Author: Mark Spicer
# Purpose: To scan a provided subnet for responsive machines

# Import the necessary modules.
import os
import nmap
import threading

# Create a scan class that creates a thread for each host
class scan (threading.Thread):
    # Create the object.
	def __init__(self, threadID, name, ip):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.ip = ip
		self.info = 0

    # Run the port scanner on the IP address.
	def run(self):
		nm = nmap.PortScanner()
		nm.scan(hosts=self.ip, arguments='-T5')
		self.info = nm

	# Return the info for the IP address.
	def results(self):
		return self.info
