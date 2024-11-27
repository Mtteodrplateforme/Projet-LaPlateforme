N = int(input("Entrez un entier supérieur à zéro (N) :"))
i = 1
while (i <= 10):
    if (N > 0):
        print(f"{N} x {i} = {N * i}")
        i += 1
    else:
        print("Veuillez saisir un nombre supérieur à zéro.")
        break