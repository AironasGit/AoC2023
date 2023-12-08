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
    endNode = 'ZZZ'
    node = 'AAA'
    count = 0
    while node != endNode:
        for instruction in instructions:
            if node == endNode:
                break
            if 'L' in instruction:
                node = nodes.get(node)[0]
                count += 1
            if 'R' in instruction:
                node = nodes.get(node)[1]
                count += 1
    answer = count
    print(answer)


if __name__ == "__main__":
    main()