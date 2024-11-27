def insert_in_list():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("melon")
    fruits.insert(2, "mangue")
    return fruits

x = insert_in_list()
print(x)