# Python Primitive Data Types
# Data Types: String, Integer, Float, Boolean
print('Hello'[-1])
num_char = len(input('What Is Your Name? '))
new_num_char = str(num_char)
print('Your name has ' + new_num_char + " characters. ")

a = float(123)
print(type(a))
print(70 + float('100.5'))
print(str(70) + str(100))


two_digit_number = input("Type a Two Digit Number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)

# Mathematical Operators
# + - * / % **
print(3 * 3 + 3 / 3 - 3)

# BMI
height = input("Enter Your Height in Meters: ")
weight = input("Enter Your Weight in Kilograms: ")
bmi = int(weight) / float(height) ** 2
print(int(bmi))

print(round(8 / 3, 2))

score = 0
length = 1.8
isWinning = True

# f-String Formatted Strings

print(f'Your Score is {score}, Your height is {length}, You are {isWinning}')

age = input('What is your current age? ')
age_in_weeks = int(age) * 52
print(f'Your age in weeks is {age_in_weeks}')

# Tip Calculator
print('Welcome to the Tip Calculator')
bill = float(input('What was the Total Bill? $'))
tip = int(input('How Much Tip Would You Like to Give? 10, 12, or 15?'))
people = int(input('How many people to split the bill? '))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f'Each Person should pay: ${final_amount}')

