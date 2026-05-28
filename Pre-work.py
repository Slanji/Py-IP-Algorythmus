import math

inputbasisnetz = input("Wie lautet die Basisnetz? (Beispiel: 192.168.0.0) ")
inputnetzanzahl = int(input("Wie viele Subnetze möchtest du haben? "))
inputhostanzahl = int(input("Wie viele Geräte sollen in ein Netz? "))

# Subnetzmaske = 225.255.255.192


total = 0
bit = math.ceil(math.log2(inputhostanzahl))
hostanzahl = 2 ** bit
netze = 256 / inputnetzanzahl

for count in range(inputnetzanzahl):
    total += hostanzahl
    parts = inputbasisnetz.split('.')
    parts[3] = f'{total}'
    new_ip = '.'.join(parts)

    if total > 256:
        print(f"Fehler: Maximum an IPs erreicht")
        break
    elif hostanzahl > netze:
        print("Fehler: Zu viele Subnetzmasken und zu wenige IPs")
        break
    else:
        print(f"Vergebare IPs: {new_ip}")
