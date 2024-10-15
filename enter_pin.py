print("BANK OF CODÉDEX")

pin= int(input("Enter your pin: "))
count=0




while pin!= 1234:
    pin = int(input(str(f"Incorrect pin. {str(3-count)} more attempts left. \n Enter your PIN again: ")))
    count+= 1 
    if count==3:
        print("Locked out.")
        exit()
        
if pin == 1234:
    print('PIN accepted!')
    
        