import random
print("Welcome to the game of rock-paper-scissor")
print("Rules of the game: \n rock beats scissor,scissor beats paper and paper beats rock")
while True :
    print("Your Choice: \n 1. rock \n 2. paper \n 3.scissor \n")
    choice = int(input("Enter 1,2 or 3:"))
    comp_choice = random.randint(1,3)
    while (comp_choice == choice):
        comp_choice = random.randint(1,3)
    print ("computer chose :" + str(comp_choice))
    if choice == 1:
        name = "rock"
    elif choice == 2:
        name = "paper"
    else:
        name = "scissor"
    if (choice == 1 and comp_choice==2) or ( choice==2 and comp_choice==1):
        print("paper beats rock")
        result = "paper"
    elif (choice == 2 and comp_choice== 3) or (choice == 3 and comp_choice==2):
        print("scissor beats paper")
        result = "scissor"
    else:
        print("rock beats scissor")
        result = "rock"
    if result == name:
        print("Congratulations! You won")
    else:
        print("oops!! Computer won.")
    ans = input("Do you wish to play again? (Y/N)")
    if ans == "n" or ans == "N":
        break
