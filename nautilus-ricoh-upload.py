#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
This nautilus script uses ricoh-upload.py to upload files to RICOH printers (e.g. http://drucker.uni-hd.de).
"""

import os, sys

USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'
PATH = '/usr/local/bin/ricoh-upload.py'

def notify(title, text):
	os.system('notify-send ' + '\"' + str(title) + '\" \"' + str(text) + '\"')

filelist = sys.argv[1:]
cmd = PATH + ' --username ' + USERNAME + ' --password ' + PASSWORD

for filename in filelist:
	cmd += ' ' + filename

os.system(cmd)

notify('RICOH Upload', 'Das Hochladen wurde erfolgreich abgeschlossen.')
