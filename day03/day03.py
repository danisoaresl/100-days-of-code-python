#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))

#if height == 120:
#    print("You can ride the rollercoaster")
#else:
#    print("Sorry you have to grow taller before you can ride.")

#Even  number 12 / 2 == 0
#Even number 12 % 2 == 0

#number_to_check = int(input("What is the number you want to check?"))

#if number_to_check % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm?"))
#bill = 0

#if height >= 120:
#    print("You can ride the rollercoaster")
#    age = int(input("What is your age? "))
#    if age <= 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18:
#        bill = 7
#        print("Youth tickets are $7. ")
#    else:
#        bill = 12
#        print("Adult tickets are $12. ")

#    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#    if wants_photo == "y":
#        # Add $3 to their bill
#        bill += 3 

#    print(f"Your final bill is ${bill}") 
#else:
#    print("Sorry you have to grow taller before you can ride.")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")