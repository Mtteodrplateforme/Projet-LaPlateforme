def plateau_affichage(p):
    print(f"{p[0]} | {p[1]} | {p[2]}")
    print("---------")
    print(f"{p[3]} | {p[4]} | {p[5]}")
    print("---------")
    print(f"{p[6]} | {p[7]} | {p[8]}")

def cas_victoire_erreur(plateau, joueur):
    gagnant = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinaison in gagnant:
        if (all(plateau[i] == joueur for i in combinaison)):
            return True
    return False

def jeu():
    plt = [' ' for _ in range(9)]
    joueur = 'X'
    while True:
        plateau_affichage(plt)
        print(f"Tour de {joueur}")
        try:
            case = int(input("Entrez un numéro de case (0 à 8) : "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
            continue
        
        if (case < 0 or case > 8 or plt[case] != ' '):
            print("Case invalide ou déjà occupée. Essayez une autre.")
            continue
        plt[case] = joueur
        
        if (cas_victoire_erreur(plt, joueur)):
            plateau_affichage(plt)
            print(f"Félicitations ! Le joueur {joueur} a gagné !")
            break
        
        if (' ' not in plt):
            plateau_affichage(plt)
            print("C'est un match nul !")
            break
        joueur = 'O' if joueur == 'X' else 'X'

jeu()