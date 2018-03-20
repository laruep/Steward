"""
@author: Paul LaRue
Steward Chat Parser

"""
import sys
import datetime

#import csv

# file name passed in from CMD
chat = sys.argv[1]
# wednesday or sunday shift
shift = sys.argv[2]

# globals -- lists
date = []
name = []
reqpairs = []

def getTimeStamp(line):
	tmp = line
	tmp = tmp.split(',',3)
	tmp = tmp[1]
	tmp = tmp.split(' ')

	date = tmp[0]
	time = tmp[1]

	date = datetime.datetime.strptime(date+' '+time, '%Y-%m-%d %H:%M:%S')
	now = datetime.datetime.now()

	diff = now - date
	datetime.timedelta(0,8,562000)
	print divmod(diff.days * 86400 + diff.seconds, 60)
	#print date
	



if __name__ == "__main__":
	with open(chat) as f:
		content = f.readlines()

	getTimeStamp(content[0])

"""
# Find third comma and split string, remove extraneous shit
reqp = content[0].split(',',3)
reqp.pop(0)
reqp.pop(0)
reqp.pop(0)

reqt = (reqp[0].rsplit(',',1))[0]
reqt = reqt.strip('\"')
reqf = (reqp[0].rsplit(',',1))[1]
reqf = reqf.replace('\n','')
reqf = int(reqf)
#print reqt
#print reqf

reqpairs.append((reqt,reqf))

print reqpairs[0]
"""


# get the timestamp (date/time) for a request 




# get the request text and # of favs into a tuple
#def getReqPair(line):
	#blep