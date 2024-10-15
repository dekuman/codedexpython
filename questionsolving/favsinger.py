
n= 7
string= '23 35 84 20 20 6 6'

list1= string.split(' ')

setlist= set(list1)

newlist= list(setlist)

newn= len(setlist)
ans=0
print("Till here")
#i=0
for i in range(newn):
    print('i=',i)
    l=int(newlist[i])
    count=0
    c=0
    print("Till for")

    while c!=n:
        #print(c)
        print('list-',list1[c])
        if int(list1[c])==l:
            count=count+1
            print('brr',count)
        c=c+1
        print("Till while")
        
    if count>=n/2-0.5:
        ans=ans+1
        print('answer=', ans)    

    

print("He has ",ans,"favourite singers") 

print(newlist)               
    
    
    
   # print (i,list[i])
    #if int(list[i])== i:
    #    print(True)
   # else:
     #   print(False)
        
        
    
    
    
    




#print(string)

#print(animals)

#print(list)

#print(list[2])