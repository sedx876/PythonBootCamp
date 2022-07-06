# Control Flow if/else statements and Conditional Operators
print('Welcome to the RollerCoaster!!!')
height = int(input('What is Your height in cm? '))

# if height >= 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('You CANNOT ride the rollercoaster')

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is Your Age? '))
    if age < 12:
        print('Please Pay $5.')
    elif age <= 18:
        print('Please Pay $7.')
    else:
        print('Please Pay $12.')
else:
    print('You CANNOT ride the rollercoaster')


number = int(input('Please Enter a Number: '))

if number % 2 == 0:
    print('This Number is Even')
else:
    print('This Number is Odd')


length = float(input('Enter Your Height in M: '))
weight = float(input('Enter Your Weight in Kg: '))

bmi = round(weight / length ** 2)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, You are underweight')
elif bmi < 25:
    print(f'Your BMI is {bmi}, You are normal weight')
elif bmi < 30:
    print(f'Your BMI is {bmi}, You are overweight')
elif bmi < 35:
    print(f'Your BMI is {bmi}, You are obese')
else:
    print(f'Your BMI is {bmi}, You are clinically obese')

year = int(input('What Year Do You Want To Check: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year')
        else:
            print('Not Leap Year')
    else:
        print('Leap Year')
else:
    print('Not a Leap Year')