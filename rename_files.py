#
# I had some files that were created with timestamps from the wrong time zone. Used this to modify them back to something of value
# 
# For example:
# ┌─[null@overseer] - [~/simple-py] - [Mon Sep 16, 12:24]
# └─[$] <git:(master*)> python rename_files.py
# * Renaming 2013-09-16-17-15-02-inbound.json to 2013-09-16-06:15-02-inbound.json
# ...
# * Renaming 2013-09-16-20-30-07-inbound.json to 2013-09-16-09:30-07-inbound.json

import os, time, re
for f in os.listdir("output"):
	mt = time.ctime(os.path.getmtime('output/'+f))
	newfile = re.sub(r"2013-09-16-\d+\-\d+","2013-09-16-" + mt[11:16], f)
	print "* Renaming " + f + " to " + newfile 
	os.rename("output/"+f,"output/"+newfile)

