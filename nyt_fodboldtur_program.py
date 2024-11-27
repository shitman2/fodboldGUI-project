import pickle
import os
#hello
filename = 'betalinger2.pk'

if not os.path.exists(filename):
    fodboldtur = {}
else:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)

def afslut():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    print("Programmet er afsluttet")

def printliste():
    print("Betaleren har betalt følgende:")
    for key, value in fodboldtur.items():
        print(f"{key}: {value} kr.")
        remaining = 4500 - value
        if remaining == 0:
            print("Betaling fuldført.")
        else:
            print(f"Beløb tilbage at betale: {remaining} kr.")

def registrer_betaling():
    print("Registrer betaling:")
    medlem = input("Indtast medlemsnavn: ")
    if medlem in fodboldtur:
        beloeb = int(input("Indtast betalt beløb: "))
        fodboldtur[medlem] += beloeb
        print(f"{beloeb} kr. registreret for {medlem}.")
    else:
        print("Ugyldigt medlemsnavn.")

def gem():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    print("Data er blevet gemt.")

def tre_mest_manglende_betaling():
    if not fodboldtur:
        print("Ingen data tilgængelig.")
        return

    sorted_members = sorted(fodboldtur.items(), key=lambda item: item[1])
    top_three = sorted_members[:3]

    print("De tre medlemmer, der har mest tilbage at betale:")
    for medlem, betalt in top_three:
        resterende = 4500 - betalt
        print(f"{medlem}: Har betalt {betalt} kr. og mangler at betale {resterende} kr.")

def menu():
    while True:
        print("MENU")
        print("1: Print liste")
        print("2: Registrer betaling")
        print("3: Gem data")
        print("4: Vis de tre medlemmer, der har mest tilbage at betale")
        print("5: Afslut program")
        valg = input("Indtast dit valg (1-5): ")
        if valg == '1':
            printliste()
        elif valg == '2':
            registrer_betaling()
        elif valg == '3':
            gem()
        elif valg == '4':
            tre_mest_manglende_betaling()
        elif valg == '5':
            afslut()
            break
        else:
            print("Ugyldigt valg. Prøv igen.")

menu()