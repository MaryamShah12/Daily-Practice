'''
Check Whether a Year is a Leap Year or Not in Python
Given an integer input as the year, the objective is to Check if a Year is a Leap Year or Not in Python Language. To do so we’ll check each condition mentioned below in the blue box. It either of the conditions is satisfied, the year is a leap year. It’s not otherwise. Here are some methods to check whether or not it’s a leap year

Method 1: Using if-else statements 1
Method 2: Using if-else statements 2
Method 3 : Using Ternary Operator
Method 4 : Using Calendar Mode
Method 5 : Using Lamda Function
'''

import calendar
year=int(input("Enter a year to know it is leap or not"))


ans=lambda year: "leap year" if year%400==0 or (year%4==0 and year%100!=0)else "not a leap year"



'''
def leap(year):
    if calendar.isleap(year):
        return "Leap year"
    return "not a leap year"
'''


'''
def leap(year):
    return "leap year" if year%400==0 or (year%4==0 and year%100!=0)else "not a leap year"

'''








def leap(year):
    if year%400==0:
        return "leap"
    elif year%100==0:
        return "not a leap year"
    elif year%4==0:
        return "leap"

    return "not a leap year"


    
print(ans(year))
