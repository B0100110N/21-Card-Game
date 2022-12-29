# 21 card game
# well, not exactly the same, but the same concept

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
while cardAmount != 21:

    randomCard = random.choice(["♣ clubAce ♣", "♣ clubTwo ♣ ", "♣ clubThree ♣ ", "♣ clubFour ♣", "♣ clubFive ♣", "♣ clubSix ♣", "♣ clubSeven ♣", "♣ clubEight ♣", "♣ clubNine ♣", "♣ clubTen ♣", "♣J clubJack ♣J", "♣Q clubQueen ♣Q", "♣K clubKing ♣K" "♥ heartAce ♥", "♥ heartTwo ♥", "♥ heartThree  ♥", "♥ heartFour ♥", "♥ heartFive ♥", "♥ heartSix ♥", "♥ heartSeven ♥", "♥ heartEight ♥", "♥ heartNine ♥", "♥ heartTen ♥", "♥J heartJack ♥J", "♥Q heartQueen ♥Q", "♥K heartKing ♥K" "♠ spadeAce ♠", "♠ spadeTwo ♠", "♠ spadeThree ♠", "♠ spadeFour ♠", "♠ spadeFive ♠", "♠ spadeSix ♠", "♠ spadeSeven ♠", "♠ spadeEight ♠", "♠ spadeNine ♠", "♠ spadeTen ♠", "♠J spadeJack ♠J", "♠Q spadeQueen ♠Q", " ♠K spadeKing ♠K" "♦ diamondAce ♦", "♦ diamondTwo ♦", "♦ diamondThree ♦", "♦ diamondFour ♦", "♦ diamondFive ♦", "♦ diamondSix ♦", "♦ diamondSeven ♦", "♦ diamondEight ♦", "♦ diamondNine ♦", "♦ diamondTen ♦", "♦J diamondJack ♦J", "♦Q diamondQueen ♦Q", "♦K diamondKing ♦K"])
    dealUser = input("Type 'deal' to be dealt a card: ")
    print('\n')
    print("Press 'e' to exit. ")

    
    if dealUser.lower().startswith('d'):

        if randomCard == "♣ clubAce ♣":
            print("You drew an Ace of Club's.")
            clubAceInput = input("Would you like to keep 1 or 11?: ")
            if clubAceInput == "1":
                cardAmount += 1
            elif clubAceInput == '11':
                cardAmount += 11
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
        elif randomCard == "♣J clubJack ♣J":
            print("You drew a Jack of Club's.")
            cardAmount += 10
        elif randomCard == "♣Q clubQueen ♣Q":
            print("You drew a Queen of Club's.")
            cardAmount += 10
        elif randomCard == "♣K clubKing ♣K":
            print("You drew a King of Club's.")
            cardAmount += 10
            
            
        elif randomCard == "♥ heartAce ♥":   
            print("You drew an Ace of Heart's.")
            heartAceInput = input("Would you like to keep 1 or 11?: ")
            if heartAceInput == "1":
                cardAmount += 1
            elif heartAceInput == '11':
                cardAmount += 11
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
        elif randomCard == "♥J heartJack ♥J":
            print("You drew a Jack of Heart's.")
            cardAmount += 10
        elif randomCard == "♥Q heartQueen ♥Q":
            print("You drew a Queen of Heart's.")
            cardAmount += 10
        elif randomCard == "♥K heartKing ♣K":
            print("You drew a King of Heart's.")
            cardAmount += 10

            
        elif randomCard == "♠ spadeAce ♠":   
            print("You drew an Ace of Spade's.")
            spadeAceInput = input("Would you like to keep 1 or 11?: ")
            if spadeAceInput == "1":
                cardAmount += 1
            elif spadeAceInput == '11':
                cardAmount += 11
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
        elif randomCard  == "♠J spadeJack ♠J":  
            print("You drew a Jack of Spade's.")
            cardAmount += 10
        elif randomCard  == "♠Q spadeQueen ♠Q":  
            print("You drew a Queen of Spade's.")
            cardAmount += 10
        elif randomCard  == "♠K spadeKing ♠K":  
            print("You drew a King of Spade's.")
            cardAmount += 10

        
        elif randomCard == "♦ diamondAce ♦":   
            print("You drew an Ace of Diamond's.")
            diamondAceInput = input("Would you like to keep 1 or 11?: ")
            if diamondAceInput == "1":
                cardAmount += 1
            elif diamondAceInput == '11':
                cardAmount += 11
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
        elif randomCard  == "♦J diamondJack ♦J":  
            print("You drew a Jack of Diamond's.")
            cardAmount += 10    
        elif randomCard  == "♦Q diamondQueen ♦Q":  
            print("You drew a Queen of Diamond's.")
            cardAmount += 10
        elif randomCard  == "♦K diamondKing ♦K":  
            print("You drew a King of Diamond's.")
            cardAmount += 10    
                
                
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
    
