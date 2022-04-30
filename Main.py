import random
import os
from Art import logo

Card_Dictionary = {"10" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2, "1" : 1, "K" : 10, "J" : 10, "Q" : 10}
Card_List = ["J", "Q", "K", "A", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1",]


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def Your_Del_Card():
    Card = random.choice(Card_List)
    global YourPoint
    if Card == 'A':
        if YourPoint <= 10:
            YourPoint += 11
        else:
            YourPoint += 1
    else:    
        YourPoint += Card_Dictionary[Card]
    return Card
        
def Computer_Del_Cards():
    Card = random.choice(Card_List)
    global ComputerPoint
    if Card == 'A':
        if ComputerPoint <= 10:
            ComputerPoint += 11
        else:
            ComputerPoint += 1
    else:    
        ComputerPoint += Card_Dictionary[Card]
    return Card


while True:
    clearConsole()
    print(logo)
    
    Your_Cards = []
    Computer_Cards = []
    
    YourPoint = 0
    ComputerPoint = 0
    
    FirstDel = True

    while True:
        if FirstDel:
            Your_Cards.append(Your_Del_Card())
            Your_Cards.append(Your_Del_Card())
            
            Computer_Cards.append(Computer_Del_Cards())
            Computer_Cards.append(Computer_Del_Cards())
            
            FirstDel = False
        else:
            Your_Cards.append(Your_Del_Card())


        print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
        print(f"Computer Card : [{Computer_Cards[0]}]")

        if YourPoint > 21:
            clearConsole()
            print(logo)
            print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
            print(f"Computer Cards are : [{', '.join(Computer_Cards)}] --> Score : {ComputerPoint}")
            print("You Lose!")
            break
        if YourPoint == 21:
            clearConsole()
            print(logo)
            print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
            print(f"Computer Cards are : [{', '.join(Computer_Cards)}] --> Score : {ComputerPoint}")
            print("Congratulation! You are BlackJack")
            break
        
        another = input("Type 'y' to get another card, type 'n' to pass : ")
        clearConsole()
        print(logo)
        
        if another == 'n':
            while ComputerPoint < 17:
                Computer_Cards.append(Computer_Del_Cards())
            
            if YourPoint == ComputerPoint:
                clearConsole()
                print(logo)
                print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
                print(f"Computer Cards are : [{', '.join(Computer_Cards)}] --> Score : {ComputerPoint}")
                print("Draw")
            elif ComputerPoint == 21:
                clearConsole()
                print(logo)
                print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
                print(f"Computer Cards are : [{', '.join(Computer_Cards)}] --> Score : {ComputerPoint}")
                print("You Lose!")
            elif YourPoint > ComputerPoint:
                clearConsole()
                print(logo)
                print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
                print(f"Computer Cards are : [{', '.join(Computer_Cards)}] --> Score : {ComputerPoint}")
                print("You Win!")
                
            else:
                clearConsole()
                print(logo)
                print(f"Your Cards are : [{', '.join(Your_Cards)}] --> Score : {YourPoint}")
                print(f"Computer Cards are : [{', '.join(Computer_Cards)}] --> Score : {ComputerPoint}")
                print("You Lose!")
            break
        
    isContinue = input("\nDo you want to play agan ? (Y/N) : ")
    if isContinue.lower() == 'n':
        break
print("\n\n\t\tThank You For Playing This Game!\n\n")