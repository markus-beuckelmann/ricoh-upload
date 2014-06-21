ricoh-upload
============

Upload files to [RICOH](http://www.ricoh.com) printers (e.g. [http://drucker.uni-hd.de](http://drucker.uni-hd.de)) using the web interface.

Installation
------------

For installation, simply download ricoh-upload.py to a directory of your choice and make it exectuable.

If you are using [Nautilus](http://wiki.gnome.org/Nautilus) file manager, you can use the enclosed nautilus script. Here are the installation steps:

1. Download nautilus-ricoh-upload.py to a directory of your choice
2. Edit `PATH`, `USERNAME` and `PASSWORD` in nautilus-ricoh-upload.py
3. Create a symlink from `~/.gnome2/nautilus-scripts` to ricoh-upload.py:
`cd ~/.gnome2/nautilus-scripts/; ln -s /usr/local/bin/nautilus-ricoh-upload.py "Upload to RICOH server"`
4. To upload file(s): Select file(s) -> Right-click -> Scripts -> Upload to RICOH server

If you are using [Thunar](http://docs.xfce.org/xfce/thunar/start) file manager, go have a look at [Thunar's custom actions](http://docs.xfce.org/xfce/thunar/custom-actions).

Requirements
------------

Please install the python packages [mechanize](http://pypi.python.org/pypi/mechanize/) and [optparse](http://docs.python.org/2/library/optparse.html):

`sudo pip install mechanize optparse`
