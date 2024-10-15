import random

symbols= ['🍒',' 🍇', '🍉', '7️⃣']


def play():
    print("\t\t\tWelcome to the Daily Slot")
    ch= True
    times_played=0
    while(ch is not False):
        ch= input("Would you like to play again?(Y/N)- " if times_played>0 else "Would you like to play?(Y/N)- " )
        if ch == 'Y' or ch=='y':
            times_played= times_played+1
            print("\tKa-Ching\nLoading...\n")
            results= random.choices(symbols, k=3)
            
            if results==[ '7️⃣', '7️⃣', '7️⃣']:
                print(results)
                print("YOU HIT THE JACKPOT!!!")
                
            else:
               print(results)
               print("Thanks for playing!") 
               
        else:
            ch=False


play()           
                       
            
            
        
        