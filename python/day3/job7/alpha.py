alphabet = "abcdefghijklmnopqrstuvwxyz"*10

x = 1
y = 0

while y + x <= len(alphabet):
    print(alphabet[y:y+x])
    x+=1
    y+=1