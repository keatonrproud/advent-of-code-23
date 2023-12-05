with open('sample.txt') as f:
    data = [l.strip() for l in f.readlines() if l.strip()]

data[0] = [int(n) for n in data[0].split(' ')[1:]]
starts = data[0][1::2]
ends = data[0][::2]
d = {'seeds': list(zip(starts, ends))}

soil_map = data.index('seed-to-soil map:')
soil_fert_map = data.index('soil-to-fertilizer map:')
fert_water_map = data.index('fertilizer-to-water map:')
water_light_map = data.index('water-to-light map:')
light_temp_map = data.index('light-to-temperature map:')
temp_humidity_map = data.index('temperature-to-humidity map:')
humidity_loc_map = data.index('humidity-to-location map:')

soil_map = data[soil_map+1:soil_fert_map]
soil_fert_map = data[soil_fert_map+1:fert_water_map]
fert_water_map = data[fert_water_map+1:water_light_map]
water_light_map = data[water_light_map+1:light_temp_map]
light_temp_map = data[light_temp_map+1:temp_humidity_map]
temp_humidity_map = data[temp_humidity_map+1:humidity_loc_map]
humidity_loc_map = data[humidity_loc_map+1:]

names = ['seed-soil', 'soil-fert', 'fert-water', 'water-light', 'light-temp', 'temp-humidity', 'humidity-loc']
for map, name in zip((soil_map, soil_fert_map, fert_water_map, water_light_map, light_temp_map, temp_humidity_map, humidity_loc_map), names):
    dat = {}
    for m in map:
        dest, source, length = m.split()
        dat[(int(source), int(length)+int(source))] = int(dest)

    covered_seeds = list(dat.keys())

    # account for seed #s not accounted for
    for s, e in d['seeds']:
        for seed in range(s, e+1):
            for (c, l) in covered_seeds:
                if seed < c or seed >= l:
                    dat[(seed, seed+1)] = seed

    covered_seeds = list(dat.keys())
    # account for prev map #s not accounted for
    if names.index(name) != 0:
        prev_outputs = d[names[names.index(name)-1]].values()
        for o in prev_outputs:
            for (c, l) in covered_seeds:   # 2
                if o < c or o >= l:
                    dat[(o, o+1)] = o

    d[name] = dat

min_loc = 10000000000000000000000000000000000000000000

for s, e in d['seeds']:
    for source in range(s, e+1):
        for name in names:
            for _, (c, l) in enumerate(d[name].keys()):
                if c <= source < l:
                    source = d[name][(c, l)] + (source-c)
                    break

    if source < min_loc: min_loc = source

print('==================')
print('LOWEST LOC', min_loc)