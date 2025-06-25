import random as rn
from time import *
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "A",
         "2", "3", "4", "5", "6", "7", "8", "9", "A",
         "2", "3", "4", "5", "6", "7", "8", "9", "A",
         "2", "3", "4", "5", "6", "7", "8", "9", "A",]

def getCrad():
    card = rn.choice(cards)
    cards.remove(card)
    return(card)

userCards = []
dealerCards = []

action = input()

def summ(arr):
    total = 0
    for i in arr:
        if i == "A":
            total += (11)
        else:
            total += int(i)
    return total

def dealersAction(cards):
    if summ(cards) <= 10:
        return "More"
    elif summ(cards) <= 15:
        if rn.randint(1, 10) <= 7:
            return "More"
        else:
            return "Check"
    elif summ(cards) <= 20:
        if rn.randint(1, 10) <= 9:
            return "More"
        else:
            return "Check"
    elif summ(cards) >= 21:
        return("Check")


def status(userCards, dealerCards):
    print("-----------------------------------------------------------------------------")
    print("Dealer`s cards:", "hidden", *dealerCards[1:])
    print("Your`s cards:", *userCards, "Total:" , summ(userCards))
    print("Actions:")
    print("Check More EndGame")
    print("-----------------------------------------------------------------------------")

def getCard():
    card = rn.choice(cards)
    cards.remove(card)
    return card

def endStatus():
    for i in range(1, 4):
        print("*" * i)
        sleep(.5)
    print("Dealer`s cards:", dealerCards, "Total:", summ(dealerCards))
    print("Your`s cards:", userCards, "Total:", summ(userCards))
#############################
dealerCards.append(getCard())
dealerCards.append(getCard())
############################# start cards for dealer and user
userCards.append(getCard())
userCards.append(getCard())
#############################


while action != "EndGame":
    dealerCardsSum = summ(dealerCards)
    userCardsSum = summ(userCards)
    status(userCards, dealerCards)
    if dealerCardsSum > 21:
        endStatus()
        print("You WON!")
        break
    elif userCardsSum > 21:
        print("You LOST!")
        break
    if summ(userCards) < 21:
        # print(dealerCards, userCards)
        action = input("Your action:")

        if action == "More":
            userCards.append(getCard())
        dealersAct = dealersAction(dealerCards)
        if dealersAct == "More":
            dealerCards.append(getCard())
        print("Dealer`s action:", dealersAct)

        if dealersAct == "Check" and action == "Check":

            if dealerCardsSum > userCardsSum and (dealerCardsSum <= 21 and userCardsSum <=21):
                endStatus()
                print("You LOST!")
                break
            elif dealerCardsSum < userCardsSum:
                endStatus()
                print("You WON!")
                break

            else:
                endStatus()
                print("DRAW!")
                break
        sleep(2)