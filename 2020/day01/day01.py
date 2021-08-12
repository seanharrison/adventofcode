import os

PATH = os.path.dirname(os.path.abspath(__file__))
with open(PATH + "/input.txt") as f:
    data = [int(l.strip()) for l in f.readlines()]

for a in data:
    b = 2020 - a
    if b in data:
        print(a, "*", b, "=", a * b)
        break

found = False
for i, a in enumerate(data):
    for j, b in enumerate(data[i + 1 :]):
        k = i + j + 1
        c = 2020 - a - b
        if c in data[k:]:
            print(a, "*", b, "*", c, "=", a * b * c)
            found = True
            break
    if found is True:
        break
