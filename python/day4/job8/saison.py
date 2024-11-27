def saison_fruit(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise et cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Conditions non remplies")

saison_fruit("légume", "feur")