
class City:
    def __init__(self,name, country, population, landmarks):
        self.name= name
        self.country= country
        self.population= population
        self.landmarks= landmarks
        
tvm= City('Trivandrum','India',2984000,["Secretariate","Zoo","Museum","Castle"])
delhi= City("Delhi","India",33807000,["Qutub Miinar","Lotus Temple","India Gate"])
sydney= City("Sydney","Australia",5185000,["Sydney Opera House","Sydney Harbour Bridge","Bondi Beach"])        
        
print(vars(tvm))
print(vars(delhi))
print(vars(sydney))
