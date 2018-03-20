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
shift = sys.argv[2]              # <--- ENABLE WHEN NEEDED

# globals -- lists
# May need one big ass list full of tuples (minutesAgo, request, favorites) 
# Then cutoff the requests from last shopping shift 
LIST = []

date = []
name = []
reqpairs = []

def getTimeStamp(line):
	# @return - minutes from NOW to request timestamp
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
	ret = divmod(diff.days * 86400 + diff.seconds, 60)

	# Returning minutes of timedelta from NOW to request time
	# Should only keep requests within 3-4 days of script to make sure its relevant

	#DEBUG
	#print ret[0]

	return ret[0]

def getReqPair(line):
	# split up line
	tmp = line
	tmp = tmp.split(',',3)

	# pop unnecessary info (chatname,timestamp, user)
	tmp.pop(0)
	tmp.pop(0)
	tmp.pop(0)

	reqt = (tmp[0].rsplit(',',1))[0]
	reqt = reqt.strip('\"')
	reqf = (tmp[0].rsplit(',',1))[1]
	reqf = reqf.replace('\n','')
	reqf = int(reqf)

	return [reqt,reqf]


################################################################

# Cut off requests from list that are past last shopping shift
def removeRequest(list):
	# wed = 4320 ... sun = 5760
	if shift == 'wed':
		cutoff = 4320
	elif shift == 'sun':
		cutoff = 5760

	list_size = len(list)
	idx_max = list_size - 1

	i = 0
	while i <= idx_max:
		# minutesAgo is held in 0 index
		if list[i][0] > cutoff:
			#remove old requests
			list.pop(i)
			#remove one from size of list
			idx_max -= 1
			#dont increment
		else:
			i += 1







#################################################################

def populateList(file):
	with open(file) as f:
		content = f.readlines()
	# content is a list with each index as a line of text

	for i in content:
		tmp_time = getTimeStamp(i)    # minutes ago
		tmp_reqp = getReqPair(i)
		tmp_req = tmp_reqp[0]         # request
		tmp_fav = tmp_reqp[1]         # favorites

		LIST.append( (tmp_time,tmp_req,tmp_fav) )



##################################################################






if __name__ == "__main__":
	populateList(chat)

	# At this point, LIST is full of tuples
	removeRequest(LIST)

	#DEBUG
	for i in LIST:
		print i






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

