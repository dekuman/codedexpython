import datetime as dt
import bday_messages

today= dt.date.today()
next_birthday= dt.date(2024,9,11)

days_away= next_birthday-today

if today==next_birthday:
    print (bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!') 
    

       


