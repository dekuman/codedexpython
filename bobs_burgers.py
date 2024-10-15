
class Restraunt:
    name= ''
    category= ''
    rating= 0.0
    delivery= False
    

bobs_burgers= Restraunt()
bobs_burgers.name= 'Bob\'s Burgers'
bobs_burgers.category= 'American Diner'
bobs_burgers.rating= 4.7
bobs_burgers.delivery= False 


kfc= Restraunt()
kfc.name= 'Kentucky Fried Chicken'
kfc.category= "American Fast Food"
kfc.rating= 2.7
kfc.delivery= True

south_indian= Restraunt()
south_indian.name='South Indian'
south_indian.category= 'Indian Diner'
south_indian.rating= 3.1
south_indian.delivery= False

print(vars(bobs_burgers))
print(vars(kfc))
print(vars(south_indian))










   