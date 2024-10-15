import random

roll= random.randint(1,9)

qn= input("Whats your Question: ")


if roll==1:
    ans= "Yes - Definitely."
elif roll==2:
        ans= "It is decidedly so."
elif roll==3:
        ans= "Without a doubt."
elif roll==4:
        ans= "Reply hazy, try again."               
elif roll==5:
        ans= "Ask again later."
elif roll==6:
        ans= "Better not tell you now."        
elif roll==7:
        ans= "My sources say no."
elif roll==8:
        ans= "Outlook not so good."         
else :
        ans= "Very doubtful."
        

print("Question:      ",qn)
print("Magic 8 Ball:  ",ans)  
      
        
                 