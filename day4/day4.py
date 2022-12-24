def part1():
    filename = "day4\day4.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    total_count =  0

    for line in lines:
        first_elf,second_elf  = line.split(',')
        first_elf_range = list(range(int(first_elf.split('-')[0]),int(first_elf.split('-')[1])+1))
        second_elf_range = list(range(int(second_elf.split('-')[0]),int(second_elf.split('-')[1])+1))
        

        if set(first_elf_range).issubset(second_elf_range) or set(second_elf_range).issubset(first_elf_range) :
            total_count+=1
    
    return total_count

def part2():
    filename = "day4\day4.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    total_count =  0

    for line in lines:
        first_elf,second_elf  = line.split(',')
        first_elf_range = list(range(int(first_elf.split('-')[0]),int(first_elf.split('-')[1])+1))
        second_elf_range = list(range(int(second_elf.split('-')[0]),int(second_elf.split('-')[1])+1))
        

        if len(list(set(first_elf_range).intersection(second_elf_range))) > 0  :
            total_count+=1
    
    return total_count

print(part1())
print(part2())