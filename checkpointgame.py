import random

print("\t\t\t__________ MISCRIT RUMBLE __________")
print("In the world where humans and miscrits((creatures from the wild with supernatural powers( pika..?) ), live together- \n")
print("You are an adventurer that trains your beloved crit- Chimpfire(a fire/beast miscrit) ")
print("You were heading towards a training gym in a far off city, having to make your way through Elmorse Forest, a huge forest a lot of wild miscrits call home")
print("You're carefully making your way through the forest with your party, when you encounter a wild pack of Miscrits")
print("Your party engages in battle,and you are facing a dangerous earth/beast miscrit- the Faunabear \n")
print("And your only way out of this is to win- \n")
print("FIGHT")


hp= 100     
npchp=100


playerturn= True
defeat= False

spcounter=2
special=1
spattack=0

while defeat is not True:
    
    if playerturn == True:
        print("\n\nChimpfire's turn to attack- \n")
        print(f"1.Heatwave (Disables Faunabear from attacking for 2 turns) {special} use left \n2.Torchkick (10) \n3.Special attack- Flamefist (30), {spcounter}","use left" if (spcounter==1) else "uses left")
        attack=int(input("\nChoose your attack- "))
        
        if attack==1:
            if special>0:
                print("You choose Heatwave")
                spattack=2
                print(f"Chimpfire performs Heatwave")
                special=special-1
            else:
                print("Chimpfire can't use the technique again, turn to attack lost")    
            
        if attack==2:
            print("You choose Torchkick") 
            npchp= npchp-10
            print(f"Attack lands \n*Faunabear burns* HP -10")
                                                                    
        if attack==3:
            if spcounter>0:
                print("You choose SPECIAL ATTACK Flamefist")
                npchp= npchp-30
                print(f"Attack lands \n*Faunabear gets knocked to the ground* HP -30")  
                spcounter= spcounter-1
            else:
                print("Chimpfire doesnt have enough vitality to perform attack, Faunabear takes the opportunity to counter")
        
        print(f"Faunabear HP-",(npchp if (npchp>0) else "0"))
        
        if hp <= 0 or npchp <= 0:            
            defeat= True
                
        playerturn= False
    
    
    elif spattack>0:
        print("Faunabear is drowsy and unable to attack")
        spattack= spattack-1
        playerturn= True
        
           
    else :
        print("\n\nFaunabear's turn to attack- \n")   
        npc_attack= random.randrange(1,4,1)        
        
        if npc_attack==1:
            print("Faunabear chose Leafthrow")
            hp= hp-10
            print(f"Attack lands \n*Chimpfire tumbles down* HP -10")
            
        if npc_attack==2:
            print("Faunabear chose Greenbeam")
            hp= hp-15
            print(f"Attack lands \n*Chimpfire gets hit* HP -15")    
             
        if npc_attack==3:
                print("Faunabear chose SPECIAL ATTACK Ragebite")
                hp= hp-30
                print(f"Attack lands \n*Chimpfire falls to the ground* HP -30")
                
        print(f"Chimpfire's HP-",(hp if (hp>0) else "0"))
        
        if hp <= 0 or npchp <= 0:
            defeat= True
                
        playerturn= True
       
        
if hp<=0:
    print("\n\nChimpfire is defeated \nTry again. ")
elif npchp<=0:
    print("\n\nFaunabear is defeated, you helped save your team adventurer.")
else:
    print("Error")    
            
            
        
