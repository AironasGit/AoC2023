def main():
    with open('Day5/input.txt') as file:
        lines = file.readlines()
    seeds = []
    toMap = []
    for i, line in enumerate(lines):
        if i == 0:
            seeds = list(map(int ,line.split(': ')[1].split()))
            continue
        if line.split() != []:
            if line.split()[0].isdigit():
                toMap.append(list(map(int, line.split())))
        if line == '\n' or i == len(lines) - 1:
            if toMap != []:
                destinationRangeStart = 0
                sourceRangeStart = 0
                rangeLength = 0
                isFound = [False for i in range(len(seeds))]
                for mapRow in toMap:
                    destinationRangeStart = mapRow[0]
                    sourceRangeStart = mapRow[1]
                    rangeLength = mapRow[2]
                    for j in range(len(seeds)):
                        if not isFound[j]:
                            if seeds[j] >= sourceRangeStart and seeds[j] <= sourceRangeStart + rangeLength - 1:
                                seeds[j] = destinationRangeStart + (seeds[j] - sourceRangeStart)
                                isFound[j] = True
                toMap.clear()
    answer = min(seeds)
    print(answer)


if __name__ == "__main__":
    main()