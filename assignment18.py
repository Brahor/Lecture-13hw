class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        
        new_name = f"{self.name} {other_country.name}"
        new_population = self.population + other_country.population
        
        return Country(new_name, new_population)


kievan = Country('Kievan', 10_000_000)
rus = Country('Rus', 50_000_000_000)


kievan_rus = kievan.add(rus)

print(kievan_rus.population)  
print(kievan_rus.name)        
