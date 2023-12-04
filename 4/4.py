with open('input.txt') as f:
    data = [[x for x in l.strip().split(':')[1].split(' ')[1:] if x] for l in f.readlines()]

d = {}
for i, x in enumerate(data):
    have = True
    have_nums = set()
    winning_nums = set()
    for num in x:
        if num == '|':
            have = False
            continue
        have_nums.add(int(num)) if have else winning_nums.add(int(num))
    d[i+1] = {'have': have_nums, 'winning': winning_nums}


## for points
total_pts = 0
for key in d.keys():
    haves = d[key]['have']
    winnings = d[key]['winning']
    winners = haves.intersection(winnings)

    total_pts += 2**(len(winners)-1) if len(winners) else 0


## for scratchcards
total_cards = 0
instance_dict = {k: 1 for k in d.keys()}
match_dict = {k: 0 for k in d.keys()}
for key in d.keys():
    matches = len(d[key]['have'].intersection(d[key]['winning']))
    match_dict[key] = matches
    for n in range(1, matches+1):
        instance_dict[key+n] += instance_dict[key]
    total_cards += instance_dict[key]

print(instance_dict)
print(match_dict)
print(total_cards)
