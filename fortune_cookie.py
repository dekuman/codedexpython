import random


def fortune():
    rn=random.randint(0,7)
    
    Fortune_list=["Don't pursue happiness - create it.","All things are difficult before they are easy.","The early bird gets the worm, but the second mouse gets the cheese.",
            "Someone in your life needs a letter from you.", "Don't just think. Act!","Your heart will skip a beat.","The fortune you search for is in another cookie.",
            "Help! I'm being held prisoner in a Chinese bakery!"]
    print(rn)
    print(Fortune_list[rn])
    
    
    '''
    if rn==1:
        print("Don't pursue happiness - create it.")
    elif rn==2: 
        print("All things are difficult before they are easy.")    
    elif rn==3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif rn==4:
        print("Someone in your life needs a letter from you.")
    elif rn==5:
        print("Don't just think. Act!")
    elif rn==6:
        print("Your heart will skip a beat.")
    elif rn==7:
        print("The fortune you search for is in another cookie.")
    else:
        print("Help! I'm being held prisoner in a Chinese bakery!")   
        
       ''' 
 
 
fortune()                
                    
    
    
    






