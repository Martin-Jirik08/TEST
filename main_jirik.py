# Importing all app imports
from config_jirik import *

# Main Window Functions
def calculate_cml(hmotnost, af):
    bmr = hmotnost * 24.2
    cml = bmr * af
    cml = round(cml, 2)
    return cml
def user_choice(us_choice):
    user_messaage = "Your choice is: " + us_choice
    return user_messaage


# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries
#import knihoven
from random import randint



