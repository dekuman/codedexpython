
gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

qn1= int(input(" Q1) Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n"))

if qn1==1:
    gryffindor+=1 
    ravenclaw+=1 
elif qn1==2:
    hufflepuff+=1
    slytherin+=1
else:
    print("Error, Choose the options correctly")
    exit(0)
    
    
qn2= int(input(" Q2) When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n"))

if qn2==1:
    hufflepuff+=2
elif qn2==2:
    slytherin+=2
elif qn2==3:
    ravenclaw+=2
elif qn2==4:
    gryffindor+=2      
else:
    print("Error, Choose the options correctly")
    exit(0)


qn3= int(input(" Q3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n"))

if qn3==1:
    slytherin+=4
elif qn3==2:
    hufflepuff+=4
elif qn3==3:
    ravenclaw+=4
elif qn3==4:
    gryffindor+=4      
else:
    print("Error, Choose the options correctly")
    exit(0)
    
if gryffindor>slytherin and gryffindor>hufflepuff and gryffindor>ravenclaw:
    print("The Sorting Hat has chosen your house as... GRYFFINDOR")   
    
elif slytherin>gryffindor and slytherin>hufflepuff and slytherin>ravenclaw:
    print("The Sorting Hat has chosen your house as... SLYTHERIN")

elif ravenclaw>gryffindor and ravenclaw>hufflepuff and ravenclaw>slytherin:
    print("The Sorting Hat has chosen your house as... RAVENCLAW")  
    
elif hufflepuff>gryffindor and hufflepuff>slytherin and hufflepuff>ravenclaw:
    print("The Sorting Hat has chosen your house as... HUFFLEPUFF")          


exit(0)