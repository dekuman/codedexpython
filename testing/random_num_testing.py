import random

i=0
count= [0,0,0]
others=0
for i in range(100):
    npc_attack= random.randrange(1,4,1)
    if npc_attack==1:
        count[0]=count[0]+1
    elif npc_attack==2:
        count[1]=count[1]+1   
    elif npc_attack==3:
        count[2]=count[2]+1
    else:
       others=others+1          
    print(npc_attack)

print("number of 1's= ", count[0]) 
print("number of 2's= ", count[1])   
print("number of 3's= ", count[2])
print("number of others= ", others)    


    
 
   
    