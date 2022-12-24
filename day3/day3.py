import string
import numpy as np

def part1():
    filename = "day3\day3.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    
    total_score = 0
    for line in lines:
        first_half = line[:int(len(line)/2)]
        second_half = line[int(len(line)/2):]



        common_item = set(first_half).intersection(second_half)
        
        if list(common_item)[0].islower():
            total_score += string.ascii_lowercase.index(list(common_item)[0])+1
        else:
            total_score += (string.ascii_uppercase.index(list(common_item)[0]) + 27)

    return total_score

print(part1())

def part2():
    filename = "day3\day3.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
        num_of_groups = len(lines)/3
        groups = np.split(np.array(lines),num_of_groups)
    
    total_score = 0
    for group in groups:
        common_item = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
        
        if common_item.islower():
            total_score += string.ascii_lowercase.index(common_item)+1
        else:
            total_score += (string.ascii_uppercase.index(common_item) + 27)

    return total_score
        

print(part2())