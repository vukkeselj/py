while True:
    broj=int (input("Unesi broj: "))
    if broj > 0 and broj < 9:
        break
print(broj)

inc = 0

for x in range(broj):
    inc += 1
    broj -= 1
    print(" " * broj + "#" * inc + "  " + "#" * inc + " " * broj)
    











