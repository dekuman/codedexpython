Binary=[]
a= int(input("Enter number: "))
while a>0:
    b=a
    if b % 2 == 0:
        Binary.append('0')
    else:
        Binary.append('1')
    a=b//2
result=Binary[::-1]

resultstr= ''.join(result)


print (resultstr)
    
  