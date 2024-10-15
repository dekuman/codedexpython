
'''print("Welcome to a Day in the life of Kazuma")

print("Kazuma is a higschool student- a well rounded one who's good at his studies and sports, and he lives a simple life, everyday as normal as the previous one")
print("And other than a slight feeling of weirdness he's been having for a few days, everything is going good in his life.")
print("---------------------------------------------------------------------------------------------------------------------------------")
print("And here is another normal Monday in his life- ")
print("Your job as the player will be to help make Kazuma choices in his life, so that he has yet another good day in life")
print("Make the best of choices and stick with it player!")'''

conf= 10
lazy= 10
energy= 20
heal= 10
hyg= 10
intel= 10
style= 10
comm= 10
luck= 10
ss= 10




print("*Kazuma wakes up from sleep*")
print('Kazuma- "... uhh...what time is it?"')

ch1 =int(input('\n<1.To check phone  \n 2.To go back to sleep> - '))
if ch1== 1:
    print('"Oh its still 7 am, I only have to leave for school at 9, hmm should I..."')
    ch11 = int(input('\n<1.Go for a run \n 2.Sleep for another hour (energy +2)> - '))

    if ch11== 1:
        conf+= 1
        energy-= 1
        heal+= 2
        hyg+= 2
        
        print ('*Kazuma goes for a 45 minute run, gets back feeling alive and refreshed* (confidence +1, energy -1, health +2) ')
        print ('*Kazuma takes a shower (hygiene +2) and settles down*')
        ch111 = int(input('\n<1.Take some time to get dressed nicely, grab something quick to eat and leave  \n 2.Take some time to make a healthy breakfast, get dressed and leave > -'))
        
        if ch111== 1:
            conf+= 2
            style+= 2
            energy+= 1
            
            print('*Kazuma gets dripped out (confidence +2, style +2, energy +1) and leaves for school*')
            
        elif ch111== 2:
            energy+= 3
            heal+= 1
                
            print('*Kazuma makes a scrumptious, well rounded meal (energy +3, health +1) and leaves for school*')
            
        else :
            print('WRONG INPUT,Kazuma just got sucked into a black hole. \nGAME OVER')    
            exit()
            
        print("*Kazuma heads out to the street, nearby at a bus stop he sees other students he goes to school with waiting for the school bus*")
        print('*He usually takes a shortcut route from his home and walks to school, it has a beautiful hillside view on the way and he enjoys it*')
        print("*But he has a test today, he wants to go through some topics he hasn't and wants to revise, he could do it in the bus *")
        print('*He stands there deciding either to walk to school or take the bus*')
        
        ch112=int(input('\n<1.Take the bus so he can possibly study  \n 2.Walk to school enjoying his time > -'))
        
        if ch112== 1:
            print('*Kazuma gets on the bus* \n He takes a seat and tries to revise, but notifications pop up on his phone')
            
            ch1121= int(input('\n<1.Ignore the message and keep revising  \n 2.Respond to the notification > -'))
            
            if ch1121== 1:
                intel+= 1
                conf+= 1
                
                print('*Kazuma takes his time to revise and goes through the topics he studied already(intelligence +2, confidence +1)*')
                print('*Feeling good about his study session he gets off at school*')
                
            elif ch1121== 2:
                print("*He checks his phone, and finds out its messages in his 'boys only' group chat*")
                print("*It was banter aimed at him, and he found out that the girl he's always crushing over at school, Aqua, broke up and is currently single*")
                print('*He was finally felt hopeful, but his friends were really going in on him*')    
                print('*Kazuma jumps in on the conversation and is fully engaged with them till he reaches school (communication +1, confidence +1, social status +1), and gets off the bus to his class *')
            
            else :
                print('WRONG INPUT,Kazuma just got sucked into a black hole. \nGAME OVER')    
                exit()
                
            
    
        elif ch112== 2:
            print('*Kazuma decides to walk to school*')
            print("*It's a sunny day, the hillside looks so warm and bright, he's enjoying his walk to school*")
            print('*On his way, he notices someone walking ahead of him, and instantly realises her as Megumi, one of his oldest friends from school*')
            print("*They've always been best of friends, but after getting into a fight recently, they haven't talked to each other for 2 days*")
            print("*Kazuma wants to work things out, yet is very hesitant*")
            
            ch1122=int(input('\n<1.Enough waiting around, go and try to resolve things with Megumi  \n 2.Ignore her and wait things out > -'))
#diagwork            
            if ch1122== 1:
                
                ss+= 2
                comm+= 2
                
                print("*Kazuma decides to sort things out, he walks up behind her and calls her out*")
                print('Kazuma- "Hey Megumi, wait..."')
                print('Megumi- "Oh Kazuma! Didnt expect to see you here..."')
                print('Kazuma- "What do you mean, I usually walk this way to school"')
                print('Megumi- "Brr brr skrr"')
                print('Kazuma- "About that, I wanna fix things, we cool? (social status +2, communication +2)"')
                
                if hyg<12:
                
                    ss-= 1
                    conf-= 1
                    
                    print('Megumi- "Why does it feel like you didnt shower today?"')
                    print('Kazuma- "umm... heh, nah I did shower.. "')
                    print('Megumi- "Yea rigth" *rolls eyes*  (social status -1, confidence -1)')
                    
                print("They walk to school together and arrives on time.")
                
                
                
            elif ch1122== 2:
                print()
                 
            
              
            else : 
                print('WRONG INPUT,Kazuma just got sucked into a black hole. \nGAME OVER')    
                exit()       
                
        else :
            print('WRONG INPUT,Kazuma just got sucked into a black hole. \nGAME OVER')    
            exit()   
        
            
             
            
    elif ch11==2:
        print()
                

           
    
elif ch1==2:
    print('*yawn* Im so tired maybe I should sleep for a bi-... *snores* (laziness +3)')
    print('*Kazuma jolts awake, now really concerned about the time checks his phone*')
    print('"Oh shit its 8.30(am), I have to leave this place by 9 my god..."')
    print('*Kazuma starts rushing around*')
    
    ch21 = int(input('\n<1.Take a shower, put on something good and leave(hygiene +2, style +1, energy -1) \n 2.Skip shower, eat something good and leave (energy +2, health +1, hygiene -2)> -'))
 
else :
    print("Wrong input dumbass")     
    
      
    
    
    
    







