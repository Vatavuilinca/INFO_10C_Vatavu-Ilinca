Putere=int(input('Dati Puterea (W): '))
Timp=int(input('Dati Timpul (h): '))
Energie=Putere*Timp/1000
print(f'Spre achitare {Energie:.2f} kWh')
Tarif=float(input('Dati Tariful actual: '))
Cost=Energie*Tarif
print(f'Spre achitare {Cost:.2f} lei')