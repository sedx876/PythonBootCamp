# Control Flow if/else statements and Conditional Operators
# print('Welcome to the RollerCoaster!!!')
# height = int(input('What is Your height in cm? '))

# if height >= 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('You CANNOT ride the rollercoaster')

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is Your Age? '))
#     if age < 12:
#         print('Please Pay $5.')
#     elif age <= 18:
#         print('Please Pay $7.')
#     else:
#         print('Please Pay $12.')
# else:
#     print('You CANNOT ride the rollercoaster')


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

print('Welcome to the RollerCoaster!!!')
height = int(input('What is Your height in cm? '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is Your Age? '))
    if age < 12:
        bill = 5
        print('Child Tickets are $5.')
    elif age <= 18:
        bill = 7
        print('Youth Tickets are $7.')
    else:
        bill = 12
        print('Adult Tickets are $12.')

    wants_photo = input('Do You want a Photo? Y or N: ')
    if wants_photo == "Y" or "y":
        bill += 3
    print(f'Your Bill is ${bill}')
else:
    print('You CANNOT ride the rollercoaster')


print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza would you like to order? S, M, or L ')
add_pepperoni = input('Do You Want Pepperoni? Y or N ')
extra_cheese = input('Do You Want Extra Cheese? Y or N ')
bill = 0

if size == "S" or "s":
    bill += 15
elif size == "M" or "m":
    bill += 20
elif size == "L" or "l":
    bill += 25
else:
    bill += 0

if add_pepperoni == "Y" or "y":
    if size == "S" or "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or "y":
    bill += 1

print(f'Your bill is ${bill}')

# Logical Operators and or not

print('Welcome to the Love Calculator!!')
name1 = input('What is Your Name? \n')
name2 = input('What is their Name? \n')

combine_string = name1 + name2
lower_case_string = combine_string.lower()
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = str(true) + str(love)
if (int(love_score) < 10) or (int(love_score) > 90):
    print(f'Your Love Score is {love_score}, You go together like coke and mentos')
elif (int(love_score) >= 40) and (int(love_score) <= 50):
    print(f'Your Love Score is {love_score}, You are alright together')
else:
    print(f'Your Love Score is {love_score}')