y = x = aim = 0
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        head, dist = line.strip().split()
        dist = int(dist)
        if head == 'forward':
            x += dist
            y += dist * aim
        elif head == 'up':
            aim -= dist
        elif head == 'down':
            aim += dist

print('x', x, 'y', y, 'aim', aim, 'x*y', x*y)
