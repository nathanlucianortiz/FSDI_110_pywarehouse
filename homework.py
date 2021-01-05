import datetime
import math 

def calculate_age():
   
   year = int(input(" Please provide the year you were born: "))
   month = int(input(" Please provide the number of the month you were born. For example 3 = March: "))
   day = int(input(" Please provide the day you were born: "))
   dob = datetime.datetime(year,month,day)
   age = (datetime.datetime.now() - dob)
   convertdays = int(age.days)
   ageyears = convertdays/365
   print("*** You are " + format(ageyears, ",.0f") + " years old! ***")


def calculate_tip_tax():
   total = float(input("Please provide the total of purchase or service: $"))
   tip_tax = 0.15 * total
   print("*** Tip/Tax: $" + format(tip_tax, ",.2f"))

"""

    (To create repo)
 git init 
 git add . 
 git commit -m "class 1"

    (1st push)
 git remote add origin <GITHUB REPO URL>
 git push -u origin master

    nth push
 git add . 
 git commit -m "whatever"
 git push
"""
