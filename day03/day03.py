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



#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M or L: ")
#pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
#bill = 0
#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#elif size == "L":
#    bill += 25
#else:
#    print("You typed the wrong inputs.")

# todo: work out how much to add to their bill based on their pepperoni choice.
#if pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else:
#        bill += 3

# todo: work out their final amount on whether if they want extra cheese.
#if extra_cheese == "Y":
#    bill += 1

#print(f"Your final bill is: ${bill}.")



#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm?"))
#bill = 0

#if height >= 120:
#    print("You can ride the rollercoaster")
#    age = int(input("What is your age? "))
#    if age < 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18:
#        bill = 7
#        print("Youth tickets are $7. ")
#    elif age >= 45 and age <= 55:
#        print("Everything is going to be ok. Have a free ride on us!")
#    else:
#        bill = 12
#        print("Adult tickets are $12.")

#   wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#   if wants_photo == "y":
#        bill += 3 

#   print(f"Your final bill is ${bill}") 

#else:
#    print("Sorry, you have to grow taller before you can ride.")


# if choice1 == "left":
    # Continue in game  
# if choice1 == "right":
#    print("You fell in to a hole. Game over.")
# else:


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go?' 
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake.' 
                    'There is an island in the middle of the lake.' 
                    'Type "wait" to wait for a boat.' 
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed."
                        "There is house with 3 doors. One red,"
                        "one yellow, one blue."
                        "Which colour do you choose?\n").lower()
        # game will continue

        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:    
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
    
else:
    print("You fell in to a hole. Game Over.")