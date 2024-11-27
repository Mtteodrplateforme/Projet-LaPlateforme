def draw_triangle(hauteur):
    x = 2 * hauteur - 1
    for i in range(hauteur):
        a = hauteur - i - 1
        b = "/" + (" " * (2 * i)) + "\\" if i>0 else "/\\"
        print(" " * a + b)

draw_triangle(3)