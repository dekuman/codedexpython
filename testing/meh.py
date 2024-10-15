num=int(input())
playlist= (input().split(" "))
maxc= 0
cnt=0

for i in playlist:
    if i in playlist:
        #dictionary set 
        print()

for i in playlist:
    if i != ' ':    
        n=playlist.count(i)
        if n>= maxc:
            maxc=n
            
unq_playlist= list(set(playlist))
for i in unq_playlist:
    n=playlist.count(i)
    if n==maxc:
        cnt=cnt+1
        

print(cnt)

