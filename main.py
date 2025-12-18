with open("input2.txt", "r") as f:
    content = f.read().strip()

sum = 0
pairs = content.split(",")

for pair in pairs:
    begin, end = pair.split("-")
    for number in range(int(begin), int(end) + 1):
        s = str(number)
        lenght = len(s) 
        mid = lenght // 2
        if(lenght % 2 == 0):
            esq = s[:mid]
            dir = s[mid:]
            if(esq == dir):
                sum += number

print(sum)