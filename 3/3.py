with open('input.txt') as f:
    data = [[x for x in l.strip()] for l in f.readlines()]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spacer = '.'
allowed = numbers + [spacer]

symbols = []
for x in data:
    for y in x:
        if y not in allowed and y not in symbols: symbols.append(y)

results = {}
for ix, x in enumerate(data):
    number = ''
    loc = None
    symbol = ''
    part = False
    for iy, y in enumerate(x):
        if y.isnumeric():
            number += y
            for idx in (ix-1, ix, ix+1):
                if idx < 0 or idx >= len(data):
                    continue

                if iy > 0:
                    if data[idx][iy-1] in symbols:
                        part, loc, symbol = (True, (idx, iy-1), data[idx][iy-1])
                if iy < len(x)-1:
                    if data[idx][iy+1] in symbols:
                        part, loc, symbol = (True, (idx, iy+1), data[idx][iy+1])
                if idx != ix:
                    if data[idx][iy] in symbols:
                        part, loc, symbol = (True, (idx, iy), data[idx][iy])

        if y == spacer or y in symbols or iy == len(x)-1:
            if part and symbol:
                results[f'{loc}_{number}_{symbol}'] = {'number': int(number), 'row': loc[0], 'col': loc[1], 'symbol': symbol}
            number = ''
            loc = None
            symbol = ''
            part = False

parts = [values.get('number') for values in results.values()]


possible_gears = [v for k, v in results.items() if v.get('symbol') == '*']

gear_values = []
for i, v in enumerate(possible_gears):
    for i2, v2 in enumerate(possible_gears[i+1:]):
        if v['row'] == v2['row'] and v['col'] == v2['col']:
            gear_values.append(v['number']*v2['number'])
            print(v, v2)

print(sum(gear_values))
