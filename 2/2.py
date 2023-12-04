data = {}
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        game, vals = line.split(': ')
        vals = [v.split(', ') for v in vals.split('; ')]
        val_dict = {}
        for i, v in enumerate(vals):
            val_dict[i] = {x.split(' ')[1]:int(x.split(' ')[0]) for x in v}
        data[int(game.split(' ')[1])] = val_dict

max_reds = 12
max_greens = 13
max_blues = 14

possible = []
sets = []
for key, val in data.items():
    impossible = False
    highest_red = 0
    highest_green = 0
    highest_blue = 0

    for round, nums in val.items():
        for max_, color in ((max_reds, 'red'),
                             (max_greens, 'green'),
                             (max_blues, 'blue')):
            tot = nums.get(color, 0)
            if tot > max_:
                impossible = True
            if color == 'red':
                if tot > highest_red: highest_red = tot
            elif color == 'green':
                if tot > highest_green: highest_green = tot
            elif color == 'blue':
                if tot > highest_blue: highest_blue = tot

    sets.append(highest_red*highest_green*highest_blue)
    if not impossible: possible.append(key)

total = sum(possible)
set_total = sum(sets)

print(sets)
print(set_total)
