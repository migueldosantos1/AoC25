f = open("input1.txt", "r")

position = 50
counter = 0

for line in f:
    if line[0] == "L":
        value = int(line[1:])
        position -= value
        while position < 0:
            left = position + 100
            position = left
    else:
        value = int(line[1:])
        position += value
        while position >= 100:
            left = position - 100
            position = left
    if position == 0:
        counter += 1

print("Posição:", position)
print("Resposta:", counter)

f.close()