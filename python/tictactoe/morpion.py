def plateau_affichage(p):
    print(f"{p[0]} | {p[1]} | {p[2]}")
    print("---------")
    print(f"{p[3]} | {p[4]} | {p[5]}")
    print("---------")
    print(f"{p[6]} | {p[7]} | {p[8]}")

def jeu():
    plt = [' ' for _ in range(9)]
    plateau_affichage(plt)

jeu()