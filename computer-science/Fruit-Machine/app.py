from random import choice
from time import sleep

print("Fruit Machine")

reel = ["cherry", "bell", "lemmon", "grape"]
amountOfTimes = int(0)

# To change is looping or not
lopping = True
numberGoes = int(0)
credit = int(0)

# if user wants to play again
def playAgain():
    money = None
    lopping = True


while lopping:
    # Get random item from reel array and store it in a variole
    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)
    reel4 = choice(reel)
    money = int(input("please enter money "))
    # Take one away from money variole
    money = money - 1
    # Add one to the amount of times user has had a go
    amountOfTimes = amountOfTimes + 1
    # Print the amount of goes you have had
    print("You have had (%d) attempts" % numberGoes)
    # Print the results
    print(reel1 + " "+reel2+" "+reel3 + " "+reel4)
    # Wait two seconds
    sleep(2)
    # Change the number of goes to plus one
    numberGoes = numberGoes + 1
    # Check if user has run out of money
    if money == 0:
        print(
                "Sorry you have run out of money : ( \npay more money for more goes or play again later")
        print()
        print()
        lopping = "false"
        again = input("play again y/n ")
        if again.lower() == "y":
            playAgain()
            numberGoes = int(1)
        else:
            lopping = "false"
        # If user gets all three slots in the row
        if reel1 == reel2 and reel1 == reel3 and reel1 == reel4:
            print("Jackpot")
            credit = credit + 1
            print(credit)
            sleep(2)
            print()
            print()
            lopping = "false"
            again = input("play again y/n ")
            if again.lower() == "y":
                playAgain()
                numberGoes = int(1)
            else:
                lopping = "false"
