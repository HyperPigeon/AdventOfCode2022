import numpy as np

filename = "day1\day1.txt"
with open(filename) as f:
    lines = np.array(f.read().splitlines())

indices = np.where(lines == '')[0]

elf_calories = np.array([calorie_list[calorie_list != ''].astype(np.int32) for calorie_list in np.split(lines, indices)])
cal_sums = np.array([np.sum(calories) for calories in elf_calories])
index = np.argmax(cal_sums)
print(cal_sums[index])

cal_sums = cal_sums[np.argsort(cal_sums)]
print(sum(cal_sums[-3:]))