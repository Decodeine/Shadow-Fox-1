# A program to determine BMI category based on user input
Height = float(input('Enter height in meters: '))
Weight = float(input('Enter weight in kilograms: '))

BMI = Weight / Height**2

if BMI >= 30:
    print("Obesity")

elif BMI >= 25 and BMI < 29:
    print("Overweight")

if BMI >= 18.5 and BMI < 25:
    print("Normal")

if BMI < 18.5:
    print("underweight")

#Write a program to determine which country a city belongs to given a list of cities per country
Australia= ['Sydney','Melbourne','Brisbane','Perth']
UAE= ['Dubai','Abu Dhabi','Sharja','Ajman']
India= ['Mumbai','Bangalore','Chennai','Delhi']
User_input= input ('Enter a city name:')

if User_input in Australia:
    print("The city", User_input, "is in Australia.")
elif User_input in UAE:
    print("The city", User_input, "is in Dubai.")
elif User_input in India:
    print("The city", User_input, "is in India.")
else:
    print("City not found in the provided lists.")

#A program that takes two user inputs and determine if both inputs belong to the same country
Australia = ['Sydney', 'Melbourne', 'Brisbane', 'Perth']
UAE = ['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman']
India = ['Mumbai', 'Bangalore', 'Chennai', 'Delhi']

city_1 = input('Enter the first city name: ')
city_2 = input('Enter the second city name: ')

if city_1 in Australia and city_2 in Australia:
    print("Both cities are in Australia.")
elif city_1 in UAE and city_2 in UAE:
    print("Both cities are in the UAE.")
elif city_1 in India and city_2 in India:
    print("Both cities are in India.")
else:
    print("Both cities are not in the same country.")
