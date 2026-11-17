from enum import Enum
from pydoc import text
class Stare(Enum):
    NOU = "nou"
    LUCRU = "lucru"
    GATA = "gata"
stare: Stare = Stare(text)
print(stare.name)
print(stare.value)
print(stare == Stare.GATA)