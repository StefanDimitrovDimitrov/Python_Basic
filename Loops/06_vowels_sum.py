len = input()

sum = 0

for i in range(0, len()):
    if len[i] == "a":
        sum += 1
    if len[i] == "e":
        sum += 2
    if len[i] == "i":
        sum += 3
    if len[i] == "o":
        sum += 4
    if len[i] == "u":
        sum += 5

print(sum)
