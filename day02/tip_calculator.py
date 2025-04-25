# Subscripting
# print("Hello"[0])

# String
# print("123" + "345")

# Integer = Whole number
# print(123 + 345)

# Large Integers
# print(123_456_789)

# Float = Floating Point Number
# print(3.14159)

# Boolean
# print(True)
# print(False)

# print(int("123") + int("456"))

# int()
# float()
# str()
# bool()

# name_of_the_user = input("Enter your name")
# length_of_name = len(name_of_the_user)

# print(type("Number of letters in your name: ")) #str
# print(type(lngth_of_name)) #int

# print("Number of letters in your name: " + str(length_of_name))
      
# print("Number of letters in your name: " + len(input("Enter your name")))

# Mathematical Opetarions in Python
# print("My age: " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(5 / 3)
# print(5 // 3)
# print(2 ** 3)

# PEMDAS

# ()
# **
# * OR /
# + OR -

# print(3 * 3 + 3 / 3 - 3)
# print

# bmi = 84 / 1.65 ** 2
# print(bmi)

# print(int(bmi))

# print(round(bmi))

# print(round(bmi, 2))

# score = 0
# height = 1.8
# is_winning = True

# print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# User scores a point
# score += 1
# print(score)

# f-strings
# print("Your score is " + str(score))

# 12% = 12 / 100 = 0.12

# print(150 * 1.12 / 5)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill? "))
# bill_with_tip = bill * (1 + tip / 100) 
# print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount} ")
