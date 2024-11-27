def condition_check(x, y, z):
    if y == "/":
        return
    elif x == 0 or y == 0:
        print("Erreur")
        return
    else:
        return
    

def calcul(num1, operator, num2):
    condition_check(num1, operator, num2)
    if operator == "+":
        print(num1, operator, num2, "=", num1+num2)
    elif operator == "-":
        print(num1, operator, num2, "=", num1-num2)
    elif operator == "*":
        print(num1, operator, num2, "=", num1*num2)
    elif operator == "/":
        print(num1, operator, num2, "=", num1/num2)
    elif operator == "%":
        print(num1, operator, num2, "=", num1%num2)

calcul(2, "+", 3)
calcul(7, "-", 3)
calcul(4, "*", 3)
calcul(16, "/", 4)
calcul(10, "%", 3)