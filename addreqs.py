"""
This script will be run from CMD and allow me to quickly add new items to the growing
database of requests, so that new requests can be compared to it with fuzzywuzzy library

SHOULD USE FUZZYWUZZY TO CHECK IF ADDITIONS ARE ALREADY ON THE LIST, UNLESS I TRUST MYSELF TO BE CAREFUL TPYING LOL


----
May need optional arguments??

"""

# file in use that will be appended to, change if necessary
file = "REQUEST_DATABASE.txt"

# Prompt
print '****************************************************'
print 'THIS SCRIPT ALLOWS YOU TO ADD ITEMS TO THE DATABASE'
print '             TYPE \"exit\" to terminate'
print '****************************************************'

f = open(file,"a")
while True:
	req = raw_input("request: ")
	if req == 'exit':
		break
	else:
		f.write(req + '\n')


