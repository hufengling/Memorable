import datetime
import subprocess


# starts the "write" sequence
def write():
    if check_if_started():
        open_file(fileName="today.txt")
    else:
        parse_today()
        format_today()
        save_today()
        reset_today()
        open_file(fileName="today.txt")


# checks if entry for current day was started
def check_if_started():
    today = open("/Users/hufengling/git/Memorable/today.txt", "r")
    if today.readline() == "@@@" + get_date() + "\n":
        today.close()
        return True
    else:
        today.close()
        return False


# opens today.txt in Sublime Text
def open_file(fileName):
    subprocess.call(['open', '-a', 'Sublime Text', "/Users/hufengling/git/Memorable/" + fileName])

# parses information from today.txt
def parse_today():
    today = open("/Users/hufengling/git/Memorable/today.txt", "r")
    totalLines = today.readlines().__len__()
    today.close()

    print("totalLines = " + str(totalLines))
    dq_line_indices = []
    today = open("/Users/hufengling/git/Memorable/today.txt", "r")
    today.readline() # read the "date" line in order to skip it in following loop so we don't have to analyze it
    for lineNumber in range(0, totalLines-1):
        line = today.readline()

        if line.count("*") != 0:
            dq_line_indices += [lineNumber]
        else:
            find_at_sign(line)
    process_star_sign(dq_line_indices)

# formats today.txt to be saved to main.txt (possibly unnecessary)
def format_today():
    unformatted = True  # indicator if file was previously formatted
    today = open("/Users/hufengling/git/Memorable/today.txt", "r+")
    for line in today:
        if line == "~~~\n":
            unformatted = False
            break
    if unformatted:
        today.write("\n~~~\n")
    today.close()


# saves today.txt to main.txt
def save_today():
    main = open("/Users/hufengling/git/Memorable/main.txt", "a")
    today = open("/Users/hufengling/git/Memorable/today.txt", "r")
    for line in today:
        main.write(line)
    main.close()
    today.close()


# resets today.txt to beginning-of-day status
def reset_today():
    today = open("/Users/hufengling/git/Memorable/today.txt", "w")
    today.write("@@@" + get_date() + "\n")
    today.write(get_daily_questions())
    today.close()

# returns list of daily questions
def get_daily_questions():
    questionsString = ""
    dailyQuestions = open("/Users/hufengling/git/Memorable/daily_questions.txt", "r")
    for line in dailyQuestions:
        questionsString += line
    dailyQuestions.close()
    return questionsString


# return date (from 4AM-3:59AM)
def get_date():
    now = datetime.datetime.now()

    if now.hour < 4:
        day = now.day - 1
    else:
        day = now.day

    return "%d-%d-%d" % (now.year, now.month, day)

# find and process "@" by line
def find_at_sign(line):
    startIndex = 0 # start index of unsearched space in each line
    counter = 0
    while counter < line.count("@"):  # keeps on searching until all "@"s are found
        index = line[startIndex:].find("@")  # finds first "@" in unsearched space
        process_at_sign(line, index)  # processes that "@"

        startIndex += index + 1  # marks new beginning of unsearched space
        counter += 1  # counts number of found "@"s

# process "@"
def process_at_sign(line, index):
    return None

# process "*"
def process_star_sign(dq_line_indices):
    today = open("/Users/hufengling/git/Memorable/today.txt", "r")
    dq_line_indices += [today.readlines().__len__() - 2] # adds final
    today.close()

    today = open("/Users/hufengling/git/Memorable/today.txt", "r")
    currentDate = today.readline()
    print(currentDate)

    for initialLines in range(0, dq_line_indices[0]): # prevents bug if there is are random spaces between date and first question
        print(today.readline())

    for i in range(0, dq_line_indices.__len__() - 1):
        questionLine = today.readline()
        questionLine = reformat_question(questionLine)
        print(questionLine)

        dq = open("/Users/hufengling/git/Memorable/Daily_Questions/" + questionLine, "a")
        dq.write(currentDate)
        for line in range(dq_line_indices[i] + 1, dq_line_indices[i + 1]):
            print(today.readline())
            #dq.write(today.readline())
        dq.write("~~~\n")
        dq.close()
    today.close()

def reformat_question(questionLine):
    questionLine = questionLine.replace(" ", "_")
    questionLine = questionLine.replace("?", "")
    questionLine += ".txt"
    return questionLine

def tester():
    string = "hello"
    print(string[:4])

parse_today()
"""

def write_to_name:

def write_to_dailies:
edit for github

#create new entry and write to file by date (times from 4AM-3:59AM every day)
#find names and write to files by name along with date
#ask for Dailies and write to Dailies file (highs, lows, overall, feelings)
#for new friend, ask for birthday, location, and value of friendship
#every year, ask for new location, and value of friendship as interactions come up

"""
