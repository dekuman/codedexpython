

menu_items=['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']

def welcome():
    
    print("Hi welcome to WhackD, Our menu for today is-")
    for i in range(len(menu_items)):
        print(i+1,". ", menu_items[i])
        
def get_item(i):
    return menu_items[i-1] 

loop= True
welcome()
while loop != False:
    ch= int(input("\nEnter the menu item you want- "))
    print("\nYou got ", get_item(ch))
    more= input("\nDo you want more? Y/N-")
    if more== "Y" or more== "y":
        loop= True
    elif more== "N" or more== "n":
        print("\nThank you for shopping with us!")
        loop= False
    else:
        print("\nInvalid Choice") 
        exit
        
               
    

 


