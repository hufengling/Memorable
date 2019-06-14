import datetime
import subprocess

path = "/Users/apotharazu/Documents/GitHub/Memorable/"
import Parser

# starts the "write" sequence
def write():
    if is_started():
        open_file(fileName="Data_Files/today.txt")
    else:
        reset_temp_files()
        Parser.parse_today()
        format_today()
        save_today()
        #reset_today()
        open_file(fileName="Data_Files/today.txt")

# checks if entry for current day was started
def is_started():
    today = open(path + "Data_Files/today.txt", "r")
    if today.readline() == "@@@" + get_date() + "\n":
        today.close()
        return True
    else:
        today.close()
        return False

# opens today.txt in Sublime Text
def open_file(fileName):
    subprocess.call(['open', '-a', 'Sublime Text', path + fileName])

# delete temporary storage files
def reset_temp_files():
    return None

# formats today.txt to be saved to main.txt (possibly unnecessary)
def format_today():
    unformatted = True  # indicator if file was previously formatted
    today = open(path + "Data_Files/today.txt", "r+")
    for line in today:
        if line == "~~~\n":
            unformatted = False
            break
    if unformatted:
        today.write("\n~~~\n")
    today.close()

# saves today.txt to main.txt
def save_today():
    main = open(path + "Data_Files/main.txt", "a")
    today = open(path + "Data_Files/today.txt", "r")
    for line in today:
        main.write(line)
    main.close()
    today.close()

# resets today.txt to beginning-of-day status
def reset_today():
    today = open(path + "Data_Files/today.txt", "w")
    today.write("@@@" + get_date() + "\n")
    today.write(get_daily_questions())
    today.close()

# returns list of daily questions
def get_daily_questions():
    questionsString = ""
    dailyQuestions = open(path + "Data_Files/daily_questions.txt", "r")
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