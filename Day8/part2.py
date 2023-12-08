import math


def main():
    with open('Day8/input.txt') as file:
        lines = file.readlines()
    instructions = lines[0].strip()
    nodes = {}
    for i, line in enumerate(lines):
        if i <= 1:
            continue
        name = line.split(' = ')[0]
        left, right = line.split(' = ')[1].strip('()\n').split(', ')
        nodes[name] = (left, right)
    aNodes = []
    for node in nodes:
        if node[-1] == 'A':
            aNodes.append(node)
    counts = []
    for aNode in aNodes:
        count = 0
        while aNode[-1] != 'Z':
            for instruction in instructions:
                if aNode == 'Z':
                    break
                if 'L' in instruction:
                    aNode = nodes.get(aNode)[0]
                    count += 1
                if 'R' in instruction:
                    aNode = nodes.get(aNode)[1]
                    count += 1     
        counts.append(count)        
    answer = math.lcm(*counts)
    print(answer)


if __name__ == "__main__":
    main()