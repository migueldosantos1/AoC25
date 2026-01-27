with open("input2.txt", "r") as f:
    content = f.read().strip()

i = 0
sum = 0
pairs = content.split(",")

for pair in pairs:
    begin, end = pair.split("-")
    for number in range(int(begin), int(end) + 1):
        s = str(number)
        length = len(s)
        for number in range(1, length // 2 + 1):
            if(number == number[i + 1]):
                sum += number
            elif(number[i] == number[i + 1] and number[i + 2] == number[i + 3]):
                sum += number
            elif(number[i] == number[i + 1] and number[i + 2] == number[i + 3] and number[i + 4] == number[i + 5]):
                sum += number
            i += 1

print(sum)