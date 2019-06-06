import datetime

#return date (from 5AM-4:59AM)
def get_date():
    now = datetime.datetime.now()

    if now.hour < 5:
        day = now.day - 1
    else:
        day = now.day

    return "%d-%d-%d" % (now.year, now.month, day)

#add a new entry to a date file
def new_entry():
    currentEntry = open(get_date() + ".txt", "a")

    entry = input("Enter 'done' on own line to quit: \n")
    while entry != "done":
        currentEntry.write(entry)
        currentEntry.write("\n")
        entry = input("")

#copy paste lines from one file to another
def copy_paste(lineToCopy, fileName):
    currentEntry = open(fileName, "a")
    currentEntry.write(lineToCopy)

def prompt_dailies():
    dailies = open("dailies.txt", "r")
    for prompt in dailies:
        print(prompt)
        copy_paste(prompt, get_date() + ".txt")
        new_entry()

def write_to_name():
    print("none")
    #search for known names
    #if found:
        #open the name file
        #copy-paste the date
        #enter and copy paste the line




"""

def write_to_name:

def write_to_dailies:


#create new entry and write to file by date (times from 4AM-3:59AM every day)
#find names and write to files by name along with date
#ask for Dailies and write to Dailies file (highs, lows, overall, feelings)
#for new friend, ask for birthday, location, and value of friendship
#every year, ask for new location, and value of friendship as interactions come up

"""
