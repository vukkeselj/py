import random
pc_number = random.randint(1, 101)
print("unesi prvi pokusaj: ")
unos = int(input())
if unos == pc_number:
    print("pogodili ste")
else:
    stararazdaljina = abs(unos - pc_number)
    if stararazdaljina <= 10:
        print("Warm")
    else:
        print("Cold")
    while True:
        print("Unesi sledeci pokusaj: ")
        unos = int(input())
        if unos == pc_number:
            print("pogodili ste")
            break
        else:
            novarazdaljina = abs(unos - pc_number)
            if novarazdaljina < stararazdaljina:
                print("Warmer")
            elif stararazdaljina < novarazdaljina:
                print("Colder")
            else:
                print("Same")
            stararazdaljina = novarazdaljina
