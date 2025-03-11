#number guessing game
import random

print("Welcome to number guessing game !!!")

top = input("Enter a number: ")
if top.isdigit : 
    top = int(top)

    if top <= 0 :
        print("Enter a number greater than 0")
else:
    print("Enter positive integer next time :( ")
    quit()

random_num = random.randint(0 , top)
guesses = 0

while True:
    guesses += 1
    choice = input(f"Enter your guess betweeen 1 to {top}: ")
    if choice.isdigit : 
        choice = int(choice)
    else:
        print("Enter positive integer next time  ")
        continue

    if choice == random_num:
        print()
        print("You guess correct number!..")
        break

    elif choice > random_num:
        print("Your guess is greater than the number!")
    else :
        print("Your guess is smaller than the number!")

print("You got the number in" , guesses , "guesses")



