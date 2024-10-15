
class Pokemon():
    def __init__(self,entry: int,name: str,types:list,description:str,is_caught:bool ):
        self.entry= entry
        self.name= name
        self.types= types
        self.description= description
        self.is_caught= is_caught
        
    def speak(self):
        print(self.name,' ',self.name,'!\n')
        
    def display_details(self):
        print('Entry Number: ', self.entry)
        print('Name: ', self.name)
        print('Type: ',end="")
        for i in range(len(self.types)):
            if i>0:
                print(' ,',self.types[i],end="")
            else:
                print(self.types[i],end="")    
            
        print('\nDescription: ', self.description)
        if self.is_caught==True:
            print(self.name," has already been caught!\n")
        else:
            print(self.name," has not been caught yet!\n")    
            
        
bulbasaur= Pokemon(1,'Bulbasaur',['Grass','Poison'],'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.', True)
squirtle= Pokemon(7,'Squirtle',['Water'],'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.', True)
snom= Pokemon(872,'Snom',['Ice','Bug'],'It eats snow that has accumulated on the ground. It prefers soft, freshly fallen snow, so it will eat its way up a mountain, aiming for the peak.', False)
bronzong= Pokemon(437,'Bronzong',['Steel','Psychic'],'In ages past, this Pokémon was revered as a bringer of rain. It was found buried in the ground.', False)
clefairy= Pokemon(35,'Clefairy',['Fairy'],'On nights with a full moon, Clefairy gather from all over and dance. Bathing in moonlight makes them float.',True)

bulbasaur.speak()
bulbasaur.display_details()

squirtle.speak()
squirtle.display_details()

snom.speak()
snom.display_details()

bronzong.speak()
bronzong.display_details()

clefairy.speak()
clefairy.display_details()

    
    
    
    
