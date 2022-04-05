from random import choice
from time import sleep

#TODO: test

# Options of items
reel = ["cherry", "bell", "lemon", "grape"]

# Varible to show how many times user has played
playTimes = int(1)

# User enters in amout of money
money = int(input("Enter in a amount of money "))

# while loop varible
looping = True

# Winings varible
credit = int(money)

# For if user wants to play again
def playAgain():
    credit = int(money)
    looping = True

while looping:
    # Add 50 to credit so user gets more credits when they win
    credit = credit + 50

    # Select random reel
    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)
    reel4 = choice(reel)

    # Prints out each reel to the screen
    print(f"You have had {playTimes} rounds")
    print(reel1, reel2, reel3, reel4)
    print()

    if (reel1 == reel2 == reel3 == reel4):
        print("You Win!")
        print(f"Your winings is {credit}")
        looping = False

    # Add one to play time
    playTimes = playTimes + 1

    # MONEY
    # Take one away from the money variable
    money = money - 1

    # If money = 0 stop looping
    if money <= 0:
        print("Sorry you have run out of money : ( \npay more money for more goes or play again later")
        print()

        # If game is over ask if user wants to play again
        again = input("Play again y/n ")

        if again.lower() == "y":
            playAgain()
            money = int(input("Enter in a amount of money "))
            playTimes = int(1)
        else:
            looping = False

    # Sleep for a sceond so loop is not one afeter another
    sleep(0.2)
