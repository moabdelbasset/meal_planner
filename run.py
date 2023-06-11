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
        age_str = input("Please enter age name:\n ")
        weight_str = input("Please enter your weight in kilograms:\n")
        height_str = input("Please enter your height in meters:\n")
        print("Calculating your BMR....\n")

        # Try converting input strings to appropriate numeric types
        try:
            weight = float(weight_str)
            height = float(height_str)
            age = int(age_str)
        except ValueError:
            print("You entered non numeric data. Please try again\n")
            continue

        # Validate user info
        if not validate_user_info(weight, height, age):
            continue
        break


def validate_user_info(weight, height, age):
    """
    Validating age, height and weight and make sure they are numeric and in range
    """
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)) or not isinstance(age, (int)):
        print("You entered non numeric data. Please try again\n")
        return False
        
    elif weight < 0 or weight > 250 or height < 0 or height > 3:
        print("You entered data out of range. Please try again")
        return False
        
    else:
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
    print("Breakfast calories are", lunch_total_cals)


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
    print("Breakfast calories are", dinner_total_cals)

def main():
    """
    Run all program functions
    """
    get_data()
    calculate_breakfast()


print("Welcome to the Automatic Meal Planner")
main()
