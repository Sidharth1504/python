import random
import sys
l=[]
ans="hit me"
print("WELCOME TO BLACKJACK")
print("HERE IS YOUR DECK")
ydeck=random.randint(1,11)
ndeck=ydeck
c=random.randint(1,4)
if c==1:
    if ydeck==1:
        print("1 of hearts")
        l.append("1 of hearts")
    elif ydeck==2:
        print("2 of hearts")
        l.append("2 of hearts")
    elif ydeck==3:
        print("3 of hearts")
        l.append("3 of hearts")
    elif ydeck==4:
        print("4 of hearts")
        l.append("4 of hearts")
    elif ydeck==5:
        print("5 of hearts")
        l.append("5 of hearts")
    elif ydeck==6:
        print("6 of hearts")
        l.append("6 of hearts")
    elif ydeck==7:
        print("7 of hearts")
        l.append("7 of hearts")
    elif ydeck==8:
        print("8 of hearts")
        l.append("8 of hearts")
    elif ydeck==9:
        print("9 of hearts")
        l.append("9 of hearts")
    elif ydeck==10:
        b=random.randint(1,3)
        if b==1:
            print("King")
            l.append("king")
        elif b==2:
            print("Queen")
            l.append("Queen")
        else:
            print("Jack")
            l.append("Jack")
    else:
        ask=str(input("Ace value 2 or 11:"))
        if ask==2:
            ydeck=2
        else:
            ydeck=11
        print("Ace of Hearts")
        l.append("Ace of hearts")
elif c==2:
    if ydeck==1:
        print("1 of spades")
        l.append("1 of spades")
    elif ydeck==2:
        print("2 of spades")
        l.append("2 of spades")
    elif ydeck==3:
        print("3 of spades")
        l.append("3 of spades")
    elif ydeck==4:
        print("4 of spades")
        l.append("4 of spades")
    elif ydeck==5:
        print("5 of spades")
        l.append("5 of spades")
    elif ydeck==6:
        print("6 of spades")
        l.append("6 of spades")
    elif ydeck==7:
        print("7 of spades")
        l.append("7 of spades")
    elif ydeck==8:
        print("8 of spades")
        l.append("8 of spades")
    elif ydeck==9:
        print("9 of spades")
        l.append("9 of spades")
    elif ydeck==10:
        b=random.randint(1,3)
        if b==1:
            print("King")
            l.append("king")
        elif b==2:
            print("Queen")
            l.append("Queen")
        else:
            print("Jack")
            l.append("Jack")
    else:
        ask=str(input("Ace value 2 or 11:"))
        if ask==2:
            ydeck=2
        else:
            ydeck=11
        print("Ace of Hearts")
        l.append("Ace of hearts")
elif c==3:
    if ydeck==1:
        print("1 of diamonds")
        l.append("1 of diamonds")
    elif ydeck==2:
        print("2 of diamonds")
        l.append("2 of diamonds")
    elif ydeck==3:
        print("3 of diamonds")
        l.append("3 of diamonds")
    elif ydeck==4:
        print("4 of diamonds")
        l.append("4 of diamonds")
    elif ydeck==5:
        print("5 of diamonds")
        l.append("5 of diamonds")
    elif ydeck==6:
        print("6 of diamonds")
        l.append("6 of diamonds")
    elif ydeck==7:
        print("7 of diamonds")
        l.append("7 of diamonds")
    elif ydeck==8:
        print("8 of diamonds")
        l.append("8 of diamonds")
    elif ydeck==9:
        print("9 of diamonds")
        l.append("9 of diamonds")
    elif ydeck==10:
        b=random.randint(1,3)
        if b==1:
            print("King")
            l.append("king")
        elif b==2:
            print("Queen")
            l.append("Queen")
        else:
            print("Jack")
            l.append("Jack")
    else:
        ask=str(input("Ace value 2 or 11:"))
        if ask==2:
             ydeck=2
        else:
            ydeck=11
        print("Ace of diamonds")
        l.append("Ace of diamonds")
else:
    if ydeck==1:
        print("1 of clubs")
        l.append("1 of clubs")
    elif ydeck==2:
        print("2 of clubs")
        l.append("2 of clubs")
    elif ydeck==3:
        print("3 of clubs")
        l.append("3 of clubs")
    elif ydeck==4:
        print("4 of clubs")
        l.append("4 of clubs")
    elif ydeck==5:
        print("5 of clubs")
        l.append("5 of clubs")
    elif ydeck==6:
        print("6 of clubs")
        l.append("6 of clubs")
    elif ydeck==7:
        print("7 of clubs")
        l.append("7 of clubs")
    elif ydeck==8:
        print("8 of clubs")
        l.append("8 of clubs")
    elif ydeck==9:
        print("9 of clubs")
        l.append("9 of clubs")
    elif ydeck==10:
        b=random.randint(1,3)
        if b==1:
            print("King")
            l.append("king")
        elif b==2:
            print("Queen")
            l.append("Queen")
        else:
            print("Jack")
            l.append("Jack")
    else:
        ask=str(input("Ace value 2 or 11:"))
        if ask==2:
            ydeck=2
        else:
            ydeck=11
        print("Ace of clubs")
        l.append("Ace of clubs")    
cdeck=random.randint(1,10)
ncdeck=cdeck
times=random.randint(3,4)
#user
while ans=="hit me":
    card=random.randint(1,10)
    z=random.randint(1,4)
    if z==1:
        if card==1:
            print("1 of hearts")
            l.append("1 of hearts")
        elif card==2:
            print("2 of hearts")
            l.append("2 of hearts")
        elif card==3:
            print("3 of hearts")
            l.append("3 of hearts")
        elif card==4:
            print("4 of hearts")
            l.append("4 of hearts")
        elif card==5:
            print("5 of hearts")
            l.append("5 of hearts")
        elif card==6:
            print("6 of hearts")
            l.append("6 of hearts")
        elif card==7:
            print("7 of hearts")
            l.append("7 of hearts")
        elif card==8:
            print("8 of hearts")
            l.append("8 of hearts")
        elif card==9:
            print("9 of hearts")
            l.append("9 of hearts")
        elif card==10:
            i=random.randint(1,3)
            if i==1:
                print("King")
                l.append("King")
            elif i==2:
                print("Queen")
                l.append("Queen")
            else:
                print("Jack")
                l.append("Jack")
        else:
            ask=str(input("Ace value 2 or 11:"))
            if ans==2:
                card=2
            else:
                card=11
            print("Ace of Hearts")
            l.append("Ace of hearts")
    elif c==2:
        if card==1:
            print("1 of spades")
            l.append("1 of spades")
        elif card==2:
            print("2 of spades")
            l.append("2 of spades")
        elif card==3:
            print("3 of spades")
            l.append("3 of spades")
        elif card==4:
            print("4 of spades")
            l.append("4 of spades")
        elif card==5:
            print("5 of spades")
            l.append("5 of spades")
        elif card==6:
            print("6 of spades")
            l.append("6 of spades")
        elif card==7:
            print("7 of spades")
            l.append("7 of spades")
        elif card==8:
            print("8 of spades")
            l.append("8 of spades")
        elif card==9:
            print("9 of spades")
            l.append("9 of spades")
        elif card==10:
            i=random.randint(1,3)
            if i==1:
                print("King")
                l.append("King")
            elif i==2:
                print("Queen")
                l.append("Queen")
            else:
                print("Jack")
                l.append("Jack")
        else:
            ask=str(input("Ace value 2 or 11:"))
            if ans==2:
                card=2
            else:
                card=11
            print("Ace of spades")
            l.append("Ace of spades")
    elif z==3:
        if card==1:
            print("1 of diamonds")
            l.append("1 of diamonds ")
        elif card==2:
            print("2 of diamonds")
            l.append("2 of diamonds")
        elif card==3:
            print("3 of diamonds")
            l.append("3 of diamonds")
        elif card==4:
            print("4 of diamonds")
            l.append("4 of diamonds")
        elif card==5:
            print("5 of diamonds")
            l.append("5 of diamonds")
        elif card==6:
            print("6 of diamonds")
            l.append("6 of diamonds")
        elif card==7:
            print("7 of hearts")
            l.append("7 of hearts")
        elif card==8:
            print("8 of diamonds")
            l.append("8 of diamonds")
        elif card==9:
            print("9 of diamonds")
            l.append("9 of diamonds")
        elif card==10:
            i=random.randint(1,3)
            if i==1:
                print("King")
                l.append("King")
            elif i==2:
                print("Queen")
                l.append("Queen")
            else:
                print("Jack")
                l.append("Jack")
        else:
            ask=str(input("Ace value 2 or 11:"))
            if ans==2:
                card=2
            else:
                card=11
            print("Ace of diamonds")
            l.append("Ace of diamonds")
    else:
        if card==1:
            print("1 of clubs")
            l.append("1 of clubs")
        elif card==2:
            print("2 of clubs")
            l.append("2 of clubs")
        elif card==3:
            print("3 of clubs")
            l.append("3 of clubs")
        elif card==4:
            print("4 of clubs")
            l.append("4 of clubs")
        elif card==5:
            print("5 of clubs")
            l.append("5 of clubs")
        elif card==6:
            print("6 of clubs")
            l.append("6 of clubs")
        elif card==7:
            print("7 of clubs")
            l.append("7 of clubs")
        elif card==8:
            print("8 of clubs")
            l.append("8 of clubs")
        elif card==9:
            print("9 of clubs")
            l.append("9 of clubs")
        elif card==10:
            i=random.randint(1,3)
            if i==1:
                print("King")
                l.append("King")
            elif i==2:
                print("Queen")
                l.append("Queen")
            else:
                print("Jack")
                l.append("Jack")
        else:
            ask=str(input("Ace value 2 or 11:"))
            if ans==2:
                card=2
            else:
                card=11
            print("Ace of clubs")
            l.append("Ace of clubs")
    ndeck=ndeck+card
    print("your deck is:",l,ndeck)
    if ndeck < 21:
        pass
    elif ndeck > 21:
        print("busted")
        print("better luck next time")
        sys.exit("Game over")
        break
    else:
        print("Full set")
    ans=str(input("hit me or stay:"))
else:
    print("Your final deck is:",l,ndeck)
#comp
for i in range(1,times):
    ccard=random.randint(1,10)
    ncdeck=ncdeck+card
print("Show Deck")
print("Opp deck is:",ncdeck)
print("Your deck is",ndeck)
if ncdeck > 21:
    print("Opp lost, u won")
    sys.exit("Game over")
#showdown
if ndeck > ncdeck:
    print("You win")
elif ndeck < ncdeck:
    print("You lose")
else:
    print("tie")  
