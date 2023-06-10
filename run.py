# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials 


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Meal_Planner')


def get_data():
    """
    Get data from user and Calculate the BMI and BMR and calories intake
    """
    name_str = input("Please enter your name:\n ")
    age_str = input("Please enter age name:\n ")
    weight_str = input("Please enter your weight in kilograms:\n")
    height_str = input("Please enter your height in meters:\n")
    bmi = round(float(weight_str) / (float(height_str) * float(height_str)), 2)
    bmr = (10 * float(weight_str)) + (6.25 * float(height_str) * 100) - (5 * int(age_str)) + 5
    print(f"Your BMI is: {bmi}")
    print(f"Your recommended calories intake is: {bmr}")

    


def main():
    """
    Run all program functions
    """
    get_data()


print("Welcome to the Automatic Meal Planner")
main()   
