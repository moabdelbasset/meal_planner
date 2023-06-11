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


def calculate_protien():
    """
    Calculate the protien intake
    """
    while True:
        print("For protien choose for the following list:\n")
        print("Meat, Chicken, Eggs, Fish, Turkey, Eggs, Salmon, Shrimp, Cottage Cheese, Beans\n")
        protien_eat = input("What was your protien type:\n")
        protien_gm = input("What was your protien intake in gms:\n")
        print("Protien intake noted...\n")
        protien = SHEET.worksheet("Protien").get_all_values()
        found = False
        for row in protien:
            if row[0].lower() == protien_eat.lower():
                cals_intake = float(protien_gm) * (int(row[1]) / 100)
                print("The calories for", protien_eat, "are", cals_intake)
                found = True
                return (cals_intake)
                break
        if not found:
            print("You entered an element not found in the protien list. Please try again\n")
        

def calculate_carbs():
    """
    Calculate the carbs intake
    """
    print("For carbs choose for the following list:\n")
    print("Rice, Pasta, Bread, Oats, Potatoes, Quinoa, Corn, Milk\n")
    carbs_eat = input("What is your carbs type:\n")
    carbs_gm = input("What was your carbs intake in gms:\n")
    print("Carbs intake noted...\n")
    carbs = SHEET.worksheet("Carbs").get_all_values()
    for row in carbs:
        if row[0].lower() == carbs_eat.lower():
            #print("The calories for", carbs_eat, "are", row[1])
            cals_intake = float(carbs_gm) * (int(row[1]) / 100)
            print("The calories for", carbs_eat, "are", cals_intake)
            return (cals_intake)
            break

def calculate_fats():
    """
    Calculate the fat intake
    """
    print("For fats choose for the following list:\n")
    print("Butter, Olive oil, Coconut oil, Avocado, Almonds, Peanut butter, Cheddar cheese\n")
    fats_eat = input("What is your fat type:\n")
    fats_gm = input("What was your fat intake in gms:\n")
    fats = SHEET.worksheet("Fats").get_all_values()
    for row in fats:
        if row[0].lower() == fats_eat.lower():
            #print("The calories for", fats_eat, "are", row[1])
            cals_intake = float(fats_gm) * (int(row[1]) / 100)
            print("The calories for", fats_eat, "are", cals_intake)
            return (cals_intake)
            break



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
