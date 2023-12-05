def main():
    with open('Day5/input.txt') as file:
        lines = file.readlines()
    seeds = []
    toMap = []
    ranges = []
    for i, line in enumerate(lines):
        if i == 0:
            seeds = list(map(int ,line.split(': ')[1].split()))
            for i in range(0, len(seeds), 2):
                ranges.append([seeds[i], seeds[i] + seeds[i + 1] - 1])
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
                newRanges =[]
                for mapRow in toMap:
                    destinationRangeStart = mapRow[0]
                    sourceRangeStart = mapRow[1]
                    rangeLength = mapRow[2]
                    start = sourceRangeStart
                    end = sourceRangeStart + rangeLength - 1
                    for i, rang in enumerate(ranges):
                        if start <= rang[0] and end >= rang[0] and end <= rang[1]:
                            newRanges.append([destinationRangeStart + (rang[0] - sourceRangeStart), destinationRangeStart + (end - sourceRangeStart)])
                            ranges[i][0] = end
                        if start >= rang[0] and end <= rang[1]:
                            newRanges.append([destinationRangeStart + (start - sourceRangeStart), destinationRangeStart + (end - sourceRangeStart)])
                            ranges[i][1] = start
                            ranges.append([end, rang[1]])
                        if start >= rang[0] and start <= rang[1] and end >= rang[1]:
                            newRanges.append([destinationRangeStart + (start - sourceRangeStart), destinationRangeStart + (rang[1] - sourceRangeStart)])
                            ranges[i][1] = start
                        if start <= rang[0] and end >= rang[1]:
                            newRanges.append([destinationRangeStart + (rang[0] - sourceRangeStart), destinationRangeStart + (rang[1] - sourceRangeStart)])
                            ranges[i][0] = 0
                            ranges[i][1] = 0
                newRanges += ranges
                ranges = newRanges
                toMap.clear()
    for i, rang in enumerate(ranges):
        if rang[0] == rang[1]:
            ranges[i] = ''
        if rang[1] < rang[0]:
            ranges[i] = ''
        if rang[0] + 1 == rang[1]:
            ranges[i] = ''
    numbers = []
    for i, rang in enumerate(ranges):
        if rang != '':
            numbers.append(rang[0])
    answer = min(numbers)
    print(answer)


if __name__ == "__main__":
    main()