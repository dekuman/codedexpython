#Welcome to the mini-game adventure
#Idea: A betting game that does not end until you win or lose!
import random
#welcomes player

player_name = str(input("Hello dear traveller, welcome to The Million Dollar Club! What is your name? "))
print(f"Excellent, {player_name}! \nThe Million Dollar Club has only two rules:\n1. You must play the game.\n2. You can only leave when you have at least a million dollars!")
explain_rules = str(input("Would you like to know the rules to the game? Just say Yes or No "))

#explain rule mechanics
while (explain_rules != "No") and (explain_rules != "Yes"):
    explain_rules = str(input("Would you like to know the rules to the game? Just say Yes or No "))
if explain_rules == "No":
    print(f"You start quick, {player_name}. Let us find you an open game then, shall we?\nOh, there's one over there! Let's begin!")
elif explain_rules == "Yes":
    print("The rules are simple! At each table, there is a spacefold box with 100 galaxy marbles in it! Each marble contains a galaxy, of course.\nNow...with a little temporal magic, we will age them by millions of lightyears in just the blink of an eye!\nYour job, is to guess however many galaxies are still alive inside the box. You can bet any amount that you have, and the house will bet against you for the same amount! \nWhomever guesses the closest number to the actual number of galaxy marbles still alive, wins the whole pot! \nIf it is a draw, both parties get the money they've bet back. Simple, right?\nNow...there's an open table over there!\n Let's begin!")
#begins the game, adds money to wallet
print(f"Oh, by the way, here's 25,000 dollars, a welcome gift for you, {player_name}!")
wallet = 25_000
while wallet >= 1 and wallet < 100_000:
    print("A new round begins. \nYou see the box emptied and filled with 100 shimmering galaxy marbles, each filled with a swirling mass of brilliant stars. \nThe dealer presses a button, turning the cage walls black, and the spacefold box begins whirring. \nPlace your bets")
    bet_amount = int(input("How much do you bet?"))
    bet_alive = int(input("And how many galaxy marbles do you think are alive?"))
    house_bet = random.randint(0,100)
    galaxy_alive = random.randint(0,100)
    print(f"The house bets {house_bet}.")
    print(f"The box opens. The number of galaxy marbles still alive this round is {galaxy_alive}.")
    #draw condition
    if abs(bet_alive - galaxy_alive) == abs(house_bet - galaxy_alive):
        print("This round is a draw! Bets are returned.")
    #win condition
    elif abs(house_bet - galaxy_alive) >= abs(bet_alive - galaxy_alive):
        wallet = wallet + bet_amount
        print("You've won this round!")
    #lose condition
    else:
        wallet = wallet - bet_amount
        print("You've lost this round!")
    #end game detection
    if wallet <= 0:
        print("Sorry, you've just lost.")
        exit
    elif wallet >= 100_000:
        print(f"You've won! Congratulations, {player_name}! I hope you've had a wonderful time at the Millionaire Club.")
        exit
