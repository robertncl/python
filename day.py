# Python program to Find day of
# the week for a given date
import calendar  #module of python to provide useful fucntions related to calendar
import re  #regular expressions
import time  # module of python to parse dates


def process_date(user_input):
    user_input=re.sub(r"/", " ", user_input) #substitute / with space
    user_input=re.sub(r"-", " ", user_input) #substitute - with space
    return user_input

def find_day(date):
    # returns an integer corresponding to the day of the week
    born = time.strptime(date, '%d %m %Y').tm_wday
    # returns the day name corresponding to that integer
    return (calendar.day_name[born])

#To get the input from the user
#User may type 1/2/1999 or 1-2-1999
#To overcome those we have to process user input and make it standard
#to accept as defined by calendar and time module
user_input=str(input("Enter date     "))
date=process_date(user_input)
print("Day on " +user_input + "  is "+ find_day(date) )
