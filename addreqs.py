"""
This script will be run from CMD and allow me to quickly add new items to the growing
database of requests, so that new requests can be compared to it with fuzzywuzzy library

SHOULD USE FUZZYWUZZY TO CHECK IF ADDITIONS ARE ALREADY ON THE LIST, UNLESS I TRUST MYSELF TO BE CAREFUL TPYING LOL


----
May need optional arguments??

"""
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# file in use that will be appended to, change if necessary
file = "REQUEST_DATABASE.txt"

################################################################

def add(filename, item):

# Will open the file in 'append' mode and add the item to the end of the database
# Will also call checkDup to see if the item is already on the list or if the item 
# is very similar or perhaps a typo
# ie. Grek Yogurt --> Greek Yogurt


    # open file to read in all lines
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    # Close file
    f.close()

    # Check for duplicates,typos, etc then add it
    checkDup(filename,item)

#############################################################################

def checkDup(filename, item):
    #check new addition to be already there/typo
    reject = False
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    # Close file
    f.close()

    if len(content) == 0:
        fileAdd(filename,item)
    else:
        for i in content:
            '''
            Using fuzzywuzzy...
                if its 100 match, the item is already there, reject it
                if its close (~90?), examine it and possibly reject
                if its less (<90), try a partial fuzz ratio
                    ie. fuzz.partial_ratio("yogurt","greek yogurt") == 100
                if it doesnt pass that, its probably just different completely and should be added
            '''

            # Exact Match?
            if fuzz.ratio(i,item) == 100:
                print "Request already in database"
                # stop immediately 
                reject = True
                break

            # Close Match? 
            elif fuzz.ratio(i,item) >= 85:
                print "Request may already exist as \"" + i + "\", continue? (y/n)"
                if raw_input("r: ") == 'y':
                    reject = False
                    continue
                elif raw_input("r: ") == 'n':
                    reject = True
                    print "Rejected request\n"
                    continue
                else:
                    print "Invalid response, try again\n"

            # Partial Match? 
            elif (fuzz.ratio(i,item) < 85) and (fuzz.partial_ratio(i,item) > 85):
                print "Request is similar to another: \"" + i + "\", continue ? (y/n)"
                if raw_input() == "y":
                    reject = False
                    continue
                elif raw_input() == "n":
                    reject = True
                    print "Rejected request\n"
                    continue
                else:
                    print "Invalid response, try again\n"

            else:
                continue

            # If item is not a duplicate, typo, or similar match, add it
            if reject == False:
                fileAdd(filename, item)

################################################################################

def fileAdd(filename, item):
    f = open(filename,"a")
    f.write(item +"\n")
    f.close()
################################################################################

if __name__ == "__main__":
    # Prompt
    print '***************************************************'
    print 'THIS SCRIPT ALLOWS YOU TO ADD ITEMS TO THE DATABASE'
    print '             TYPE \"exit\" to terminate'
    print '***************************************************'

    while True:
        req = raw_input("request: ")
        if req == 'exit':
            break
        else:
            add(file,req)



