
password=input("Enter password: ")


if (password.isalnum() == False) and password.islower() == False :
    for i in password:
        if i.isnumeric() == True:
            print("Good password")
            exit()
    else:
        print("Bad Password")  
else:
        print("Bad Password")                
      