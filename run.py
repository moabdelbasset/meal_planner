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
    while True:
        name_str = input("Please enter your name:\n ")

        while True:
            try:
                age_str = input("Please enter age name:\n ")
                age = int(age_str)
                if validate_age(age):
                    break
                else:
                    print("Invalid age. Please try again.")
            except ValueError:
                print("You entered non numeric data for age. Please try again\n")

        while True:
            try:
                weight_str = input("Please enter your weight in kilograms:\n")
                weight = float(weight_str)
                if validate_weight(weight):
                    break
                else:
                    print("Invalid weight. Please try again.")
            except ValueError:
                print("You entered non numeric data for weight. Please try again\n")

        while True:
            try:
                height_str = input("Please enter your height in meters:\n")
                height = float(height_str)
                if validate_height(height):
                    break
                else:
                    print("Invalid height. Please try again.")
            except ValueError:
                print("You entered non numeric data for height. Please try again\n")
        
        print("Calculating your BMR....\n")
        #break
        bmr = calculate_bmr(weight, height, age)
        return bmr

   
def validate_weight(weight):
    """
    Function to validate weight value added by user
    """
    if weight < 0 or weight > 250:
        print("You entered data out of range. Please try again with values from 1 kg to 249 kg")
        return False
    return True

def validate_height(height):
    """
    Function to validate height value added by user
    """
    if height < 0 or height > 3:
        print("You entered data out of range. Please try again with values from 1 meters to 3 meters")
        return False
    return True

def validate_age(age):
    """
    Function to validate age value added by user
    """
    if age < 0 or age > 100:
        print("Invalid age number it should be from 1 to 100")
        return False
    return True


def calculate_bmr(weight, height, age):    
    bmi = round(float(weight) / (float(height) * float(height)), 2)
    bmr = (10 * float(weight)) + (6.25 * float(height) * 100) - (5 * int(age)) + 5
    print(f"Your BMI is: {bmi}")
    print(f"Your recommended calories intake is: {bmr}")
    return (bmr)


def calculate_protien():
    """
    Taking the protien intake from users
    """
    while True:
        print("For protien choose for the following list:\n")
        print("Meat, Chicken, Eggs, Fish, Turkey, Eggs, Salmon, Shrimp, Cottage Cheese, Beans\n")
        protien_eat = input("What was your protien type:\n")
        protien_gm = input("What was your protien intake in gms:\n")
        print("Calculating protien calories...\n")
        validate_data(protien_eat, "Protien")
        protien = SHEET.worksheet("Protien").get_all_values()
        for row in protien:
            if row[0].lower() == protien_eat.lower():
                cals_intake = float(protien_gm) * (int(row[1]) / 100)
                print("The calories for", protien_eat, "are", cals_intake)
                return (cals_intake)

        
def validate_data(data, type): 
    """
    Validating the intakes from users
    """
    list = SHEET.worksheet(type).get_all_values()            
    found = False
    for row in list:
        if row[0].lower() == data.lower():
            found = True
            return True
            break
    if not found:
        print(f"You entered an element not found in the {type} list. Please try again\n")
        return False


def calculate_carbs():
    """
    Calculate the carbs intake
    """
    while True:
        print("For carbs choose for the following list:\n")
        print("Rice, Pasta, Bread, Oats, Potatoes, Quinoa, Corn, Milk\n")
        carbs_eat = input("What is your carbs type:\n")
        carbs_gm = input("What was your carbs intake in gms:\n")
        print("Calculating protien calories...\n")
        validate_data(carbs_eat, "Carbs")
        carbs = SHEET.worksheet("Carbs").get_all_values()
        for row in carbs:
            if row[0].lower() == carbs_eat.lower():
                cals_intake = float(carbs_gm) * (int(row[1]) / 100)
                print("The calories for", carbs_eat, "are", cals_intake)
                return (cals_intake)


def calculate_fats():
    """
    Calculate the fat intake
    """
    while True:
        print("For fats choose for the following list:\n")
        print("Butter, Olive oil, Coconut oil, Avocado, Almonds, Peanut butter, Cheddar cheese\n")
        fats_eat = input("What is your fat type:\n")
        fats_gm = input("What was your fat intake in gms:\n")
        print("Calculating fats calories...\n")
        validate_data(fats_eat, "Fats")
        fats = SHEET.worksheet("Fats").get_all_values()
        for row in fats:
            if row[0].lower() == fats_eat.lower():
                cals_intake = float(fats_gm) * (int(row[1]) / 100)
                print("The calories for", fats_eat, "are", cals_intake)
                return (cals_intake)
            



def calculate_breakfast():
    """
    Calculate total calories for breakfast
    """
    print("What did you take on Breakfast?\n")
    p_cal = calculate_protien()
    c_cal = calculate_carbs()
    f_cal = calculate_fats()
    print("Calculating total calories for breakfast...\n")
    breakfast_total_cals = int(p_cal) + int(c_cal) + int(f_cal)
    print("Breakfast calories are", breakfast_total_cals)
    return breakfast_total_cals
    

def calculate_lunch():
    """
    Calculate total calories for lunch
    """
    print("What did you take on Lunch?\n")
    p_cal = calculate_protien()
    c_cal = calculate_carbs()
    f_cal = calculate_fats()
    print("Calculating total calories for lunch...\n")
    lunch_total_cals = int(p_cal) + int(c_cal) + int(f_cal)
    print("lunch calories are", lunch_total_cals)
    return lunch_total_cals


def calculate_dinner():
    """
    Calculate total calories for dinner
    """
    print("What did you take on Dinner?\n")
    p_cal = calculate_protien()
    c_cal = calculate_carbs()
    f_cal = calculate_fats()
    print("Calculating total calories for dinner...\n")
    dinner_total_cals = int(p_cal) + int(c_cal) + int(f_cal)
    print("dinner calories are", dinner_total_cals)
    return dinner_total_cals


def menu_function():
    """
    Function will print a menu for the user to either start the program
    Or read the instructions first
    """
    while True:
        print("Please select an option:")
        print("1. Instructions")
        print("2. Run Code")
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            print("Automatic Meal Planner is a program that will help you to calculate your daily caloric intake.\n"
                "Once you press 2 you will be asked to enter some information such as age, weight and height.\n"
                "Based on your entries it will calculate your BMR and start calculating your caloric intake throughout the day.\n")

        elif choice == 2:
            bmr = get_data()
            breakfast_cal = calculate_breakfast()
            lunch_cal = calculate_lunch()
            dinner_cal = calculate_dinner()
            calc_deficit(breakfast_cal, lunch_cal, dinner_cal, bmr)
        else:
            print("Invalid choice. Please enter either 1 or 2.")

def calc_deficit(breakfast_cal, lunch_cal, dinner_cal, bmr):
    """
    Calculate the caloric defincy
    """
    total_cal = breakfast_cal + lunch_cal + dinner_cal
    deficency = total_cal - bmr
    if deficency < 0:
        print(f"Good job you are on the right track having {deficency} deficency")
    else:
        print(f"You have a surplus of {deficency} calories today")


def main():
    """
    Run all program functions
    """
    print("Welcome to the Automatic Meal Planner\n")
    menu_function()
    #get_data()
    #calculate_breakfast()



main()
