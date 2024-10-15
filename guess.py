import random 

key= random.randint(1,9)
guess = 0
tries= 0

while guess != key:
  tries+= 1  
  guess = int(input('Guess the number: '))
  if guess!= key and tries!=3:
      print(f"Wrong!. Guess again you have {3-tries} tries left.")
  if tries==3 and guess!=key:
      print("Oops Game over. Play Again!")
      exit()

print("Bingo! You won the Game!") 

 