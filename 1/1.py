with open('input.txt') as f:
    d = [x.strip() for x in f.readlines()]

number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num_string_dict = dict(zip(number_strings, numbers))

total = 0
for string in d:
    nums = []
    start = 0
    for i in range(1, len(string)+1):
        part_string = string[start:i]
        char = part_string[-1]
        if char.isnumeric():
            nums.append(char)
            start = i
            continue
        for num_string in number_strings:
            if num_string in part_string:
                nums.append(num_string_dict[num_string])
                start = i-2

    cal_val = nums[0]+nums[-1] if len(nums) > 1 else nums[0]*2

    total += int(cal_val)

print(total)
