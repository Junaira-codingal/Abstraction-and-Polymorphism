class India:
    def capital(self):
        print("New Delhi is the capital of India")
        
    def Language(self):
        print("Hindi is the most widely spoken language of India")
        
    def type(self):
        print("India is a developing country")
        
class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh")
        
    def Language(self):
        print("Bangla is the most widely spoken language of Bangladesh")
        
    def type(self):
        print("Bangladesh is a developing country")
        
ind = India()
bd = Bangladesh()

for country in (ind , bd):
    country.capital()
    country.Language()
    country.type()
    
    print()