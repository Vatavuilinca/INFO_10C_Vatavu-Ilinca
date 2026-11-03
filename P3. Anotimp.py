class Anotimp(Enum):
    PRIMAVARA = 1
    VARA = 2
    TOAMNA = 3
    IARN = 4
cod1 = int(input("Introduceți primul cod (1-4): "))
cod2 = int(input("Introduceți al doilea cod (1-4): "))
anotimp1 = Anotimp(cod1)
anotimp2 = Anotimp(cod2)
print(anotimp1 == anotimp2)