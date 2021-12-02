aim = 0
hp = 0
dp = 0

with open('input.txt') as input_file:
    for line in input_file:
        if line.split()[0] == 'forward':
            hp += int(line.split()[1])
            dp += aim * int(line.split()[1])
        elif line.split()[0] == 'up':
            aim -= int(line.split()[1])
        else:
            aim += int(line.split()[1])

print("Horizontal Position:", hp)
print("Depth:", dp)

print("Horizontal position multiplied by depth:", hp * dp)
