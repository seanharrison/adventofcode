y = x = 0
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        head, dist = line.strip().split()
        dist = int(dist)
        if head == 'forward':
            x += dist
        elif head == 'up':
            y -= dist
        elif head == 'down':
            y += dist

print(x, y, x*y)
