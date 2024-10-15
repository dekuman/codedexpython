pesos= int(input('What do you have left in pesos? '))
soles= int(input('What do you have left in soles? '))
reais= int(input('What do you have left in reais? '))

peso_rate=0.00024          # Rates as of 08/29/2023
sole_rate=0.27
reai_rate=0.21

dollars=(pesos * peso_rate) + (soles * sole_rate) + (reais * reai_rate)

print('Your total in Dollars is', dollars)

