from collections import Counter

def solve(file):
    data = parseData(file)
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
    
def parseData(file):
    with open(file) as f:
        return list(map(lambda x: x.strip(), f.readlines()))

def part1(data):
    gr = ''
    ep = ''
    for item in zip(*data):
        c = Counter(item).most_common()
        gr += c[0][0]
        ep += c[1][0]
    return int(gr, 2) * int(ep, 2)

def part2(data):
    return rating(data, 1) * rating(data, 0)

def rating(data, mode):
    pos = 0
    while len(data) > 1:
        c = sorted(Counter(list(zip(*data))[pos]).most_common(),
                  key = lambda x: (x[1], x[0]))
        data = [item for item in data if item[pos] == c[mode][0]]
        pos += 1
    return int(data[0], 2)

solve('input.txt')
