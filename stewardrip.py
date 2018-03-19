"""
@author: Paul LaRue
Steward Chat Parser

"""
import sys
import csv

# file name passed in from CMD
chat = sys.argv[1]

# lists
date = []
name = []
reqpairs = []


if __name__ == "__main__":
	with open(chat) as f:
		content = f.readlines()

# Find third comma and split string
reqp = content[0].split(',',3)
reqp.pop(0)
reqp.pop(0)
reqp.pop(0)

reqt = (reqp[0].rsplit(',',1))[0]
reqf = (reqp[0].rsplit(',',1))[1]
print reqt
print reqf

reqpairs.append(())

#print req



    
	



