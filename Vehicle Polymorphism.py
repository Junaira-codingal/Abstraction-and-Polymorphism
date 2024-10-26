class Ferrari:
    
    def model(self):
        print("La Ferrari")
        
    def fuel_type(self):
        print("Petrol")
        
    def max_speed(self):
        print("Max Speed 350")
        
class BMW:
    
    def model(self):
        print("A8")
        
    def fuel_type(self):
        print("Deisel")
        
    def max_speed(self):
        print("Max Speed 240")
        
        
class BYD:
    
    def model(self):
        print("e3")
        
    def fuel_type(self):
        print("Electric")
        
    def max_speed(self):
        print("Max Speed 88 kw")
        
class Toyota:
    
    def model(self):
        print("Toyota Camry")
        
    def fuel_type(self):
        print("unleaded gasoline")
        
    def max_speed(self):
        print("Max Speed 117mph")
        
class Tesla:
    
    def model(self):
        print("Tesla Cyberquad")
        
    def fuel_type(self):
        print("Electric")
        
    def max_speed(self):
        print("Max Speed 193")
        
ferrari = Ferrari()
bmw = BMW()
byd = BYD()
toyota = Toyota()
tesla = Tesla()

for car in (ferrari , bmw , byd, toyota, tesla):
    car.model()
    car.fuel_type()
    car.max_speed()
    print()
