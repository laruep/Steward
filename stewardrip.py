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
request = []
favs = []


if __name__ == "__main__":
	with open(chat, 'rb') as csvfile:
		spamreader = csv.reader(csvfile,delimiter=',', quotechar='|')
		for row in spamreader:
			print row[3]



    
	



