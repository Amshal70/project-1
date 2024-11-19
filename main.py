import random

choices = ["snake" ,"water","gun"]
print("Welcome to Snake water Gun Game! ")
print("choose one: Snake, water or gun")

user = input("Enter your choice: ").strip().lower()

if user not in choices:
    print("Invalid choice!, please choose snake, water or gun")
    exit()

computer = random.choice(choices)
print(f"computer chose: {computer}") 

if computer == user:
    print("Its a draw!")

elif (user == "gun" and  computer=="snake") or \
     (user == "snake" and computer == "water" ) or \
     (user == "water" and computer == "gun") :
     print("you win🏆")      

else:
    print("computer wins😥")

    