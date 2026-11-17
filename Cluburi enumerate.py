from enum import Enum
class Club(Enum):
    ROBOTICA = 1
    ARTA = 2
    SPORT = 3
Cod=int=int(input("Cod="))
Alegere=Club(Cod)
print(Alegere.name)
print(Alegere.value)
