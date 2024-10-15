a= int(input('Enter the first coefficient number: '))
b= int(input('Enter the second coefficient number: '))
c= int(input('Enter the constant number: '))

root_1= (-1*b + (b**2 - 4*a*c)**0.5) / (2*a)


root_2= (-1*b - (b**2 - 4*a*c)**0.5) / (2*a)

print("First root is ", root_1)

print("Second root is ", root_2)

