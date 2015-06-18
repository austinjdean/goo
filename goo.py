#!/usr/bin/env python

import sys
import subprocess
import os
import re
import urllib2

def printHelp():
	print 'Usage:\n'
	print '\tgoo [options] [search terms]\n'
	print 'Options:\n'
	print '\t-c: open using Chrome\n'
	print '\t-f: open using Firefox\n'
	print '\t-h: display usage information\n'
	print 'Notes:'
	print '\t- search terms do not need to be enclosed in quotes.'

query = ''
browser = 'xdg-open' # system default browser - thanks: http://stackoverflow.com/questions/5116473/linux-command-to-open-url-in-default-browser
DEVNULL = open(os.devnull, 'w')

for arg in sys.argv[1:]: # skip first argument in sys.argv because it's the name of the script
	if arg == '-c':
		browser = 'google-chrome'
	elif arg == '-f':
		browser = 'firefox'
	elif arg == '--help' or arg == '-h':
		printHelp()
		exit(0)
	elif arg == '-l':
		# TODO:feeling lucky - make url to open = the first google result
		pass
	else:
		query += arg
		query += '+'

query = 'https://www.google.com/search?q=' + query

query = query[:-1] # remove final '+' added by for loop
# thanks: http://stackoverflow.com/questions/15478127/remove-final-character-from-string-python

subprocess.call([browser, query], stdout=DEVNULL, stderr=subprocess.STDOUT) # shhhh - redirect browser output to /dev/null
# thanks: http://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7