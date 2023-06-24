# Meal Planner - Portfolio Project 3

Welcome to Meal Planner, a personalized Python application designed to support and enhance your fitness journey. This innovative application is a dedicated tool to help individuals track, analyze, and plan their daily dietary requirements.

Meal Planner offers a straightforward way to calculate your daily caloric intake. By providing key details about your meals - such as type, portion size, and ingredients - the application can quickly determine your total caloric consumption for the day. The robust algorithm in place has been developed to take into account a wide range of foods, making this feature beneficial for users with diverse dietary preferences.

More than just tallying up your daily calories, Meal Planner also computes your Basal Metabolic Rate (BMR) - the number of calories your body needs to perform essential functions like breathing and maintaining body temperature while at rest. This is calculated using your age, weight, and height.

The magic of Meal Planner doesn't stop there. It goes a step further and determines whether you're in a caloric surplus or not. If you've consumed more calories than your BMR, you're in a caloric surplus - useful for those looking to gain weight or muscle. Conversely, consuming fewer calories than your BMR puts you in a caloric deficit - helpful for those aiming for weight loss.

# Design:
## User Stories
- As a user I should be able to enter my name, age, weight and height
- As a user, I want to input my age, gender, weight, and height so that the app can accurately calculate my Basal Metabolic Rate (BMR).
- As a user, I want to input my age, gender, weight, and height so that the app can accurately calculate my Basal Metabolic Index (BMI).
- As a user, I want to be able to enter my daily meals, along with their ingredients and portion sizes, so that the app can accurately calculate my daily caloric intake.
- As a user, I want to see a clear visualization of my caloric intake compared to my BMR so I can easily understand if I'm in a caloric surplus or deficit.

## Flow Chart:
![Flow Chart](doc_images/flowchart.png)    


# Features:
* Main menu:
The application has a main menu
* Instruction:
Once you run the application you have the option to start the meal planner or read the instructions first
* Input validations and error detection:
If a user enter any data the app will check if this data is valid and if its not valid it will prompt the user to enter a valid data. Data validation happens on the weight, age, height, Food list and quantity.
* Colorama:
Since its a terminal app, I used colorama to add a bit of colour where I felt was needed within the terminal to make certain parts stand out to the user. For example adding not valid data a prompt appear with color red.
* Fetching information from Google sheet:
The list of foods and it's caloric data is maintained inside a Google spreadsheet.