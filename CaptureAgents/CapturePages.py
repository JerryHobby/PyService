#######################################################################
### DEMO SCRIPT WITH VARIOUS DECLARATIONS AND EXAMPLES FOR REFERENCE

import urllib.request
import string
import os.path

from pathlib import Path
from time import sleep

## if we find StartText, we have results
## then copy that through StopText

StartText = "<span class=\"headerResults\">"
StopText = "<div class=\"footerResults\">"
FailText = "<div class=\"weAreSorry1\">"

#www.progressiveagent.com/findanagent/search-results.aspx?product=Auto&zipCode=77099


#######################################################################
### DATA DECLARATIONS

urlprefix = "http://www.progressiveagent.com/findanagent/search-results.aspx?product=Auto&zipCode="

fn_zipsfile = "C:\\Users\\Jerry Hobby\\OneDrive\\Documents\\Python\\zip_code_database.txt"
fn_outprefix = "C:\\Users\\Jerry Hobby\\OneDrive\\Documents\\Python\\progressive\\progressive-"
fn_outsuffix = ".html"

zips = []

#with open(fn_zipsfile, 'r') as f:
#	zips = f.readlines()

zips = open(fn_zipsfile).read().splitlines()
print (len(zips))

# override list for testing
zips = [ "77011", "77002", "77003", "77004", "77005"]

for zip in zips:

	url = urlprefix + zip
	print(zip + ": " + url)

	fn_name = fn_outprefix + zip + fn_outsuffix
	print(zip + ": " + fn_name)

	if not os.path.isfile(fn_name):
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req)
		html_raw = response.read()
		html_utf = html_raw.decode('utf8')

		if html_utf.find(StartText) > 0:
			openfile = open(fn_name, 'w')
			openfile.write(html_utf)
			openfile.close
			print(zip + ": Page Captured")

			for x in range(0, 10):
				print(".", end="", flush=True)
				sleep(1)			
		else:
			# create an empty file only.  easier to find/delete for retry later.
			openfile = open(fn_name, 'w')
			openfile.close

			print(zip + ": NO AGENTS FOUND")
			for x in range(0, 10):
				print("!", end="", flush=True)
				sleep(1)

		print("")

	else:
		print(zip + ": Skipping, file exists")

	print("")




