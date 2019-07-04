import Inputter

path = "/Users/apotharazu/Documents/GitHub/Memorable/"

# parses information from today.txt
def parse_today():
    dq_line_indices = []
    today = open(path + "Data_Files/today.txt", "r")
    today.readline() # read the "date" line in order to skip it in following loop so we don't have to analyze it

    # iterate through lines to count "*" and "@"
    for lineNumber in range(0, lines_in_file("Data_Files/today.txt")-1):
        line = today.readline()

        # if the line has a "*", record the line number and move on
        if line.count("*") != 0:
            dq_line_indices += [lineNumber]

        # if the line does not have a "*", look for "@"
        elif line.count("@") != 0:
            find_at_sign(line)

    # after looking through line
    process_star_sign(dq_line_indices)

# check number of lines in file
def lines_in_file(fileName):
    today = open(path + fileName, "r")
    totalLines = today.readlines().__len__()
    today.close()
    return totalLines

# find and process "@" by line
def find_at_sign(line):
    startIndex = 0 # beginning index of unsearched space in each line
    counter = 0 #counter of found "@"s

    while counter < line.count("@"):  # keeps on searching until all "@"s are found
        index = line[startIndex:].find("@")  # finds index of first "@" in unsearched space
        startIndex += index + 1  # marks new beginning of unsearched space
        counter += 1  # counts number of found "@"s

        processedLine = process_at_sign(line, startIndex)  # processes that "@"
        if processedLine:
            line = processedLine
            print(line)
        print(str(counter) + line)

# process "@"
def process_at_sign(line, index):
    if is_keyword(line, index):
        keyPhrase = process_keyword(line, index)
        return line.replace(keyPhrase, "")
    elif is_trailing_at_sign(line, index):
        return None
    else:
        write_to_temp_profile(line, index)

# check if the "@" was for a keyword
def is_keyword(line, index):
    indexOfNearestColon = line[index:].find(":")

    # if there is no ":", move on because it cannot be a keyword
    if indexOfNearestColon == -1:
        return False
    # otherwise, take string from "@" to ":"
    else:
        possibleKeyword = line[index:index + indexOfNearestColon]

    # if string is blank, it cannot be a keyword (happens with trailing "@")
    if possibleKeyword == "":
        return False

    keywords = open(path + "Data_Files/keywords.txt", "r")

    # check if possibleKeyword is in keywords.txt. If yes, then return it, if not, it is not a keyword
    for keyword in keywords:
        if keyword.find(possibleKeyword) != -1:
            keywords.close()
            return possibleKeyword

    keywords.close()
    return False

# check if "@" follows a keyword starter
def is_trailing_at_sign(line, index):
    previousAtSign = line[:index-1].rfind("@")
    # can only be a trailing @ if there is another @
    if previousAtSign != -1:
        possibleKeyPhrase = line[previousAtSign + 1:index - 1]

        # is trailing @ iff there are two colons in the possibleKeyPhrase
        if possibleKeyPhrase.find(":") != -1 and possibleKeyPhrase.rfind(":") != -1:
            return True
    return False

# process "@" if it denotes a keyword
def process_keyword(line, index):
    keyPhrase = line[index :index + 1 + line[index + 1:].find("@")] # take key phrase
    splitKeyPhrase = keyPhrase.split(":")
    currentDate = Inputter.get_date()

    profile = open(path + "Profiles/" + splitKeyPhrase[1] + ".txt", "a")
    profile.write("@@*" + currentDate + ":" + splitKeyPhrase[0] + ":" + splitKeyPhrase[2])
    profile.write("\n~~~\n")
    profile.close()

    return("@" + keyPhrase + "@")

# process "@" if it denotes a profile
def process_profile(line, index):
    write_to_temp_profile(line, index)

# writes line to temporary profile
def write_to_temp_profile(line, index):
    line = line.replace("\n", "")
    friendName = line[index:].split(" ")[0]
    profile = open(paht + "temp_files/" + friendName + ".txt", "a")
    profile.write(line)
    profile.write("\n")
    profile.close()

    temp_friends_list = open(path + "temp_files/temp_friends_list.txt", "a")
    temp_friends_list.write(friendName)
    temp_friends_list.close()

# process "*"
def process_star_sign(dq_line_indices):
    dq_line_indices += [lines_in_file("Data_Files/today.txt") - 2] # adds final line to indices

    today = open(path + "Data_Files/today.txt", "r")
    currentDate = today.readline()

    # prevents bug if there is are random spaces between date and first question
    for initialLines in range(0, dq_line_indices[0]):
        today.readline()

    # loop through text. Uses "*" lines to make/find a file. Copies text between "*" lines into appropriate file
    for i in range(0, dq_line_indices.__len__() - 1):
        # read "*" line and open/create the correct file
        questionLine = today.readline()
        questionLine = reformat_question(questionLine)
        dq = open(path + "Daily_Questions/" + questionLine, "a")

        # append date
        dq.write(currentDate)
        # add lines from the "*" line to the next one
        for line in range(dq_line_indices[i] + 1, dq_line_indices[i + 1]):
            dq.write(today.readline())
        # end the day's entry in the DQ file
        dq.write("~~~\n")
        dq.close()
    today.close()

# replace " " with "_", remove "?", and add ".txt" to end
def reformat_question(questionLine):
    questionLine = questionLine.replace(" ", "_")
    questionLine = questionLine.replace("?", "")
    fileName = questionLine.replace("\n", ".txt")
    return fileName

def tester():
    string = [True, "hello"]
    if string[0]:
        print("hello")

