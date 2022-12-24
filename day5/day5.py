import numpy as np
filename = "day5\day5_1.txt"

def part1():
    filename = "day5\day5_1.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    
    stacks = np.array([np.array(list(line)) for line in lines]).transpose()
    stacks = list(stacks[[index for index in range(1,stacks.shape[0],4)]])
    stacks = [list(stack[stack != ' ']) for stack in stacks]

    filename = "day5\day5_2.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    
    for line in lines:
        num_move = int(line.split(' ')[1])
        move_from  = int(line.split(' ')[3])-1
        move_to  = int(line.split(' ')[5])-1

        for i in range(0,int(num_move)):
            #pop item
            item = stacks[move_from].pop(0)
            #insert item 
            stacks[move_to].insert(0,item)

    top_items = [stack[0] for stack in stacks]
    return top_items

  

print(part1())

def part2():
    filename = "day5\day5_1.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    
    stacks = np.array([np.array(list(line)) for line in lines]).transpose()
    stacks = list(stacks[[index for index in range(1,stacks.shape[0],4)]])
    stacks = [stack[stack != ' '] for stack in stacks]

    filename = "day5\day5_2.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    
    for line in lines:
        num_move = int(line.split(' ')[1])
        move_from  = int(line.split(' ')[3])-1
        move_to  = int(line.split(' ')[5])-1

        #get items
        items = stacks[move_from][0:num_move]
        
        #delete items
        stacks[move_from] = stacks[move_from][num_move:]

        #insert items
        stacks[move_to] = np.insert(stacks[move_to],0,items)

    top_items = [stack[0] for stack in stacks]
    return top_items

print(part2())
        