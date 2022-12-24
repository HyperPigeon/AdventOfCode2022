
def part1():
    results = {
        ('A','X'): 4,
        ('A','Y'): 8,
        ('A','Z'): 3,
        ('B','X'): 1,
        ('B','Y'): 5,
        ('B','Z'): 9,
        ('C','X'): 7,
        ('C','Y'): 2,
        ('C','Z'): 6,
    }

    filename = "day2\day2.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    total_score = 0
    for line in lines:
        enemy_decision, player_decision = line.split(' ')
        total_score += results[enemy_decision,player_decision]

    return total_score

print(part1())

def part2():
        results = {
        ('A','X'): 3,
        ('A','Y'): 4,
        ('A','Z'): 8,
        ('B','X'): 1,
        ('B','Y'): 5,
        ('B','Z'): 9,
        ('C','X'): 2,
        ('C','Y'): 6,
        ('C','Z'): 7,
        }

        filename = "day2\day2.txt"
        with open(filename) as f:
            lines = f.read().splitlines()

        total_score = 0
        for line in lines:
            enemy_decision, player_decision = line.split(' ')
            total_score += results[enemy_decision,player_decision]

        return total_score

print(part2())