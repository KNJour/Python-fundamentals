
import random
computerScore = 0
userScore = 0
while userScore < 3 or computerScore < 3:
    userHand = input("rock, paper, or scissors?")
    x = random.randint(1,3)
    if x == 1:
        x = "rock"
    elif x == 2:
        x = "paper"
    elif x == 3:
        x = "scissors"

    if userHand == "rock":
        if x == "rock":
            print("a Tie!!")
        elif x == "paper":
            print("paper beats rock, you lose!")
            computerScore += 1
        elif x == "scissors":
            print("scissors beats paper, you win!")
            userScore += 1
    if userHand == "paper":
        if x == "paper":
            print("a Tie!!")
        elif x == "scissors":
            print("scissors beats paper, you lose!")
            computerScore += 1
        elif x == "rock":
            print("paper beats rock, you win!")
            userScore += 1
    if userHand == "scissors":
        if x == "scissors":
            print("a Tie!!")
        elif x == "rock":
            print("rock beats scissors, you lose!")
            computerScore += 1
        elif x == "paper":
            print("scissors beats paper, you win!")
            userScore += 1
    if userScore == 3:
        print("you win! Best out of 5!!")
    if computerScore == 3:
        print("you lose! Best out of 5")

