#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import mechanize
from sys import exit
from optparse import OptionParser

URL = 'http://drucker.uni-hd.de'

parser = OptionParser()
usage = 'Usage: ricoh-upload.py --username USERNAME --password PASSWORD FILE1 [FILE2] [...]'
parser = OptionParser(usage = usage)

parser.add_option('-u', '--username', action='store', dest='username', help='Provide a username.')
parser.add_option('-p', '--password', action='store', dest='password', help='Provide a password.')
(options, args) = parser.parse_args()

if not options.username or not options.password:
	print usage
	exit(1)
if not args:
	print 'No files to upload.'
	exit(0)

browser = mechanize.Browser()
response = browser.open(URL)

browser.select_form('loginform')
browser['Username'] = options.username
browser['Password'] = options.password

response = browser.submit()
content = response.read()

if 'Meine Aufträge' in browser.title():

	print 'Login successful.'
	for filename in args:
		if os.path.exists(filename):
			browser.form = list(browser.forms())[0]
			browser.form.add_file(open(filename), 'text/plain', filename)
			print 'Uploading ' + str(filename) + '...'
			response = browser.submit()
		else:
			print '"' + filename + '" does not exist.'
	print 'Done.'

else:
	print 'Login failed.'
