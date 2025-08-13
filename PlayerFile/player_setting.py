from .works_player import Work
from .countries import Countries

class Player:
    def __init__(self, name = "", age = 6, place_birth = Countries.get_countries()[0], skills = None, work = "", money = 0.0, 
                 physical_health = 100, mental_health = 50, addict = None, 
                 life = True, life_expectancy = Countries.get_countries()[1]):
        
        self.name = str(name)
        self.age = int(age)
        self.place_birth = str(place_birth) # Okay
        self.skills = skills if skills is not None else [] # Okay
        self.work = str(work)
        self.money = float(money)
        self.physical_health = physical_health
        self.mental_health = mental_health
        self.addict = list(addict) if addict is not None else []
        self.life = bool(life)
        self.life_expectancy = int(life_expectancy) # Okay 

my_player = Player()