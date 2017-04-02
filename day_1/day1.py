def turn(instruction, facing):
    if (facing == 'n'):
        if (instruction == 'R'):
            return 'e'
        else:
            return 'w'
    elif (facing == 'e'):
        if (instruction == 'R'):
            return 's'
        else:
            return 'n'
    elif (facing == 's'):
        if (instruction == 'R'):
            return 'w'
        else:
            return 'e'
    elif (facing == 'w'):
        if (instruction == 'R'):
            return 'n'
        else:
            return 's'

def move(instruction, facing, location):
    moved = location[facing]
    location[facing] = moved + instruction

location = {'n': 0, 's': 0, 'w': 0, 'e': 0}
facing = 'n'
directions = []
with open("input.dat") as f:
    directions = f.read().split(", ")

for direction in directions:
    facing = turn(direction[0], facing)
    move(int(direction[1:]), facing, location)

vertical = abs(location['n'] - location['s'])
horizontal = abs(location['w'] - location['e'])

print(vertical + horizontal)


