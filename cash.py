
while True:
    kusur=float(input("Unesite kusur: "))
    if kusur > 0:
        break
print(kusur)
cents=int(kusur*100)
print(cents)
quarter=25
dime=10
nickel=5
penny=1
coins=0

while cents>=quarter:
    cents = cents - quarter
    coins += 1

while cents>=dime:
    cents = cents - dime
    coins += 1

while cents>=nickel:
    cents = cents - nickel
    coins += 1

while cents>=penny:
    cents = cents - penny
    coins += 1

print(f"Total coins: {coins}")



