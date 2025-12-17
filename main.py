f = open("input1.txt", "r")

position = 50
counter = 0

for line in f:
    direction = line[0]
    value = int(line[1:])

    for _ in range(value):
        if direction == "L":
            position -= 1
        else:
            position += 1
        if position < 0:
            position = 99
        elif position > 99:
            position = 0
        if position == 0:
            counter += 1

print("Posição:", position)
print("Resposta:", counter)

f.close()