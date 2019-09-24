from random import randint

cont = "y"

while cont == 'y':
    number = randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != number:
        if (guess > number):
            print("Too high, try again!\n")
            guess = int(input("Guess a number between 1 and 10: "))
        else:
            print("Too low, try again!\n")
            guess = int(input("Guess a number between 1 and 10: "))
    print("You guessed it! You won!\n")
    cont = input("Do you want to keep playing? (y/n) ")
print("\nThanks for playing. Bye!")

