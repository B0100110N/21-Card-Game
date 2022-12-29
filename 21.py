# 21 card game

import random

while True: 
    
    print('\n')
    print("🃏 ♣ ♠ ♥ ♦ Welcome to 21! ♦ ♥ ♠ ♣ 🃏")
    print('\n')
    
    userInput = input("Are you ready to begin? Please type 'yes' or 'no': ")
    if userInput.lower().startswith('y'):
        break
    elif userInput.lower().startswith('n'):
        exit()



cardAmount = 0
while cardAmount != 21: #maybe while cardAmount < 0

    randomCard = random.choice(["♣ clubAce ♣", "♣ clubTwo ♣ ", "♣ clubThree ♣ ", "♣ clubFour ♣", "♣ clubFive ♣", "♣ clubSix ♣", "♣ clubSeven ♣", "♣ clubEight ♣", "♣ clubNine ♣", "♣ clubTen ♣", "♥ heartAce ♥", "♥ heartTwo ♥", "♥ heartThree  ♥", "♥ heartFour ♥", "♥ heartFive ♥", "♥ heartSix ♥", "♥ heartSeven ♥", "♥ heartEight ♥", "♥ heartNine ♥", "♥ heartTen ♥", "♠ spadeAce ♠", "♠ spadeTwo ♠", "♠ spadeThree ♠", "♠ spadeFour ♠", "♠ spadeFive ♠", "♠ spadeSix ♠", "♠ spadeSeven ♠", "♠ spadeEight ♠", "♠ spadeNine ♠", "♠ spadeTen ♠", "♦ diamondAce ♦", "♦ diamondTwo ♦", "♦ diamondThree ♦", "♦ diamondFour ♦", "♦ diamondFive ♦", "♦ diamondSix ♦", "♦ diamondSeven ♦", "♦ diamondEight ♦", "♦ diamondNine ♦", "♦ diamondTen ♦"])
    
    dealUser = input("Type 'deal' to be dealt a card: ")
    print('\n')
    print("Press 'e' to exit. ")

    if dealUser.lower().startswith('d'):

    
        if randomCard == "♣ clubAce ♣":
            print("You drew an Ace of Club's.")
            cardAmount += 1
        elif randomCard  == "♣ clubTwo ♣":
            print("You drew a Two of Club's.")
            cardAmount += 2
        elif randomCard  == "♣ clubThree ♣":
            print("You drew a Three of Club's.")
            cardAmount += 3
        elif randomCard  == "♣ clubFour ♣": 
            print("You drew a Four of Club's.")         
            cardAmount += 4
        elif randomCard  == "♣ clubFive ♣": 
            print("You drew a Five of Club's.")         
            cardAmount += 5
        elif randomCard  == "♣ clubSix ♣": 
            print("You drew a Six of Club's.")   
            cardAmount += 6
        elif randomCard  == "♣ clubSeven ♣":
            print("Your drew a Seven of Club's.")
            cardAmount += 7
        elif randomCard  == "♣ clubEight ♣":
            print("You drew an Eight of Club's.")
            cardAmount += 8
        elif randomCard  == "♣ clubNine ♣":  
            print("You drew a Nine of Club's.")        
            cardAmount += 9
        elif randomCard  == "♣ clubTen ♣": 
            print("You drew a Ten of Club's.") 
            cardAmount += 10

        elif randomCard == "♥ heartAce ♥":   
            print("You drew an Ace of Heart's.")
            cardAmount += 1
        elif randomCard  == "♥ heartTwo ♥":  
            print("You drew a Two of Heart's.")   
            cardAmount += 2
        elif randomCard  == "♥ heartThree ♥":
            print("You drew a Three of Heart's.")
            cardAmount += 3
        elif randomCard  == "♥ heartFour ♥":  
            print("You drew a Four of Heart's.")        
            cardAmount += 4
        elif randomCard  == "♥ heartFive ♥":  
            print("You drew a Five of Heart's.")        
            cardAmount += 5
        elif randomCard  == "♥ heartSix ♥":   
            print("You drew a Six of Heart's.") 
            cardAmount += 6
        elif randomCard  == "♥ heartSeven ♥":
            print("You drew a Seven of Heart's.")
            cardAmount += 7
        elif randomCard  == "♥ heartEight ♥":
            print("You drew an Eight of Heart's.")
            cardAmount += 8
        elif randomCard  == "♥ heartNine ♥":  
            print("You drew a Nine of Heart's.")        
            cardAmount += 9
        elif randomCard  == "♥ heartTen ♥":  
            print("You drew a Ten of Heart's.")
            cardAmount += 10

        elif randomCard == "♠ spadeAce ♠":   
            print("You drew an Ace of Spade's.")
            cardAmount += 1
        elif randomCard  == "♠ spadeTwo ♠":     
            print("You drew a Two of Spade's.")
            cardAmount += 2
        elif randomCard  == "♠ spadeThree ♠":
            print("You drew a Three of Spade's.")
            cardAmount += 3
        elif randomCard  == "♠ spadeFour ♠": 
            print("You drew a Four of Spade's.")         
            cardAmount += 4
        elif randomCard  == "♠ spadeFive ♠": 
            print("You drew a Five of Spade's.")         
            cardAmount += 5
        elif randomCard  == "♠ spadeSix ♠":  
            print("You drew a Six of Spade's.")  
            cardAmount += 6
        elif randomCard  == "♠ spadeSeven ♠":
            print("You drew a Seven of Spade's.")
            cardAmount += 7
        elif randomCard  == "♠ spadeEight ♠":
            print("You drew an Eight of Spade's.")
            cardAmount += 8
        elif randomCard  == "♠ spadeNine ♠": 
            print("You drew a Nine of Spade's.")         
            cardAmount += 9
        elif randomCard  == "♠ spadeTen ♠":  
            print("You drew a Ten of Spade's.")
            cardAmount += 10

        elif randomCard == "♦ diamondAce ♦":   
            print("You drew an Ace of Diamond's.")
            cardAmount += 1
        elif randomCard  == "♦ diamondTwo ♦":     
            print("You drew a Two of Diamond's.")
            cardAmount += 2 
        elif randomCard  == "♦ diamondThree ♦":
            print("You drew a Three of Diamond's.")
            cardAmount += 3
        elif randomCard  == "♦ diamondFour ♦": 
            print("You drew a Four of Diamond's.")         
            cardAmount += 4
        elif randomCard  == "♦ diamondFive ♦": 
            print("You drew a Five of Diamond's.")         
            cardAmount += 5 
        elif randomCard  == "♦ diamondSix ♦":  
            print("You drew a Six of Diamond's.")  
            cardAmount += 6
        elif randomCard  == "♦ diamondSeven ♦":
            print("You drew a Seven of Diamond's.")
            cardAmount += 7 
        elif randomCard  == "♦ diamondEight ♦":
            print("You drew an Eight of Diamond's.")
            cardAmount += 8
        elif randomCard  == "♦ diamondNine ♦": 
            print("You drew a Nine of Diamond's.")         
            cardAmount += 9
        elif randomCard  == "♦ diamondTen ♦":  
            print("You drew a Ten of Diamond's.")
            cardAmount += 10
        elif dealUser.lower().startswith('e'):
            exit()


        if cardAmount > 21:
            print('\n')
            print("You lose!")
            print(f"Your total card amount exceeded the limit (21). You had a total of {cardAmount}.")
            break
        elif cardAmount == 21:
            print('\n')
            print("21!")
            print(f"Your total adds up to {cardAmount}! Well done!")
            break     

        dealAgain = input(f"Your current card amount is {cardAmount}. Would you like to be dealt another card?: ") #syntax needs to be changed
        if dealAgain.lower().startswith('y'):
            continue
        cardAmount += cardAmount

    elif dealUser.lower().startswith('e'):
        exit()    
    
