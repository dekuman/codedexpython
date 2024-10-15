
height= int(input("Enter your height: "))
credits= int(input("Enter your credits remaining: "))

print("Calculating...")

if height>= 137 and credits>= 10:
    print("Enjoy the ride!")

elif height< 137 and credits>= 10:
    print("You are not tall enough to ride.")
    
elif height>= 137 and credits< 10:
    print("You don't have enough credits.")    
    
else:
    print("You do not meet any requirements to take the ride.")
    
    
        