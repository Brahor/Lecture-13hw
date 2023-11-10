#Task 1
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        
        new_name = f"{self.name} {other_country.name}"
        new_population = self.population + other_country.population
        
        return Country(new_name, new_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)


bosnia_herzegovina = bosnia.add(herzegovina)

print(bosnia_herzegovina.population)  
print(bosnia_herzegovina.name)        


# Task 2
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        
        new_name = f"{self.name} {other_country.name}"
        new_population = self.population + other_country.population
        
        return Country(new_name, new_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)


bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.population)  
print(bosnia_herzegovina.name)        

# Task 3
class Car:
    def __init__(self, brand, model, year, speed=2000):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed  

    def accelerate(self):
        self.speed += 5

    def brake(self):
        
        self.speed = max(0, self.speed - 5)

    def display_speed(self):
        print(f"The current speed of the {self.model} is: {self.speed} km/h")


my_car = Car('Propeler', 'Batmobile', 2028)

my_car.accelerate()
my_car.display_speed()  

my_car.brake()
my_car.display_speed()  


my_car.brake()
my_car.display_speed()  
