gameImages = ['''
    ____
    / __ \
 ( (__) |___ ___
    \________,'   """""----....____
     _______<  () dd       ____----'
    / __   __`.___-----""""
 ( (__) |
    \____/
''', '''
    8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
    88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
    88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
    88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
    88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
    88                     88                                 
    88                     88 
''', '''
    8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
    88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
    88         8b       d8 8b         8888[      
    88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
    88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
''']

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)


print(f"Computer Choice = {gameImages[computer_choice]}")

if user_choice == 0:
    if computer_choice == 0:
        print("You win, Your Rock smashes Computer's Scissors")
    elif computer_choice == 1:
        print("You lose, Computer's Paper covers Your Rock")
    else:
        print("It's a draw")
elif user_choice == 1:
    if computer_choice == 0:
        print("You loose, Computer's Scissors cuts Your Paper")
    elif computer_choice == 1:
        print("It's a draw")
    else:
        print("You win, Your Paper covers Computer's Rock")
elif user_choice == 2:
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 1:
        print("You win, Your Scissors cuts Computer's Paper")
    else:
        print("You lose, Computer's Rock smashes Your Scissors")