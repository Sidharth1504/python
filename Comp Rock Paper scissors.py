import random
ans="y"
while ans=="y":
    print("Rock")
    print("Paper")
    print("Shoot")
    rep=str(input("Enter rock paper or scissor:"))
    x=random.randint(0,100)
    if x%2==0:
        if x==2:
            a="rock"
            print("Rock")
        else:
            a="paper"
            print("Paper")
    else:
        if x==1:
            a="rock"
            print("Rock")
        else:
            for i in range(2,x):
                if (x%1) == 0:
                    a="scissor"
                    print("Scissor")
                    break
            else:
                a="rock"
                print("Rock")
    if rep=="rock" or "scissor" or "paper":
        if rep == "rock":
            if a=="scissor":
                print("You won")
            elif a=="rock":
                print("Tie")
            else:
                print("You lost")
        if rep == "scissor":
            if a=="scissor":
                print("Tie")
            elif a=="rock":
                print("You lost")
            else:
                print("You won")
        if rep == "paper":
            if a=="scissor":
                print("You lost")
            elif a=="rock":
                print("You won")
            else:
                print("Tie")
    else:
        print("invalid Input")
    ans=str(input("Do You want to play again(y/n)?:"))
else:
    print("Game Over")

