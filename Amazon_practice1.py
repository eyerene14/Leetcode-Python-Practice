from collections import Counter
logs = ["88 99 200", "88 99 300"]
d1, d2 = {},{}
if len(logs) > 1:
    for s in logs:
        line = s.split(' ')
        if line[0] == line[1]:
            d1[line[0]] += 1
        elif line[0] not in d1:
            d1[line[0]] += 1
            d1[line[1]] += 1
print(d1)
