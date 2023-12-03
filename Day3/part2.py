def main():
    with open('Day3/input.txt') as file:
        lines = file.readlines()
    input = []
    for line in lines:
        input.append(line.strip())
    numbers = []
    for i, line in enumerate(input):
        number = ''
        gearId = []
        toAdd = False
        for j, symbol in enumerate(line):
            if symbol.isdigit():
                number += symbol
                if i > 0:
                    if input[i - 1][j] == '*':
                        toAdd = True
                        gearId = [i - 1, j]
                    if j > 0:
                        if input[i - 1][j - 1] == '*':
                            toAdd = True
                            gearId = [i - 1, j - 1]
                    if j < len(line) - 1:
                        if input[i - 1][j + 1] == '*':
                            toAdd = True
                            gearId = [i - 1, j + 1]
                if j > 0:
                    if input[i][j - 1] == '*':
                        toAdd = True
                        gearId = [i, j - 1]
                if j < len(line) - 1:
                    if input[i][j + 1] == '*':
                        toAdd = True
                        gearId = [i, j + 1]
                if i < len(input) - 1:
                    if input[i + 1][j] == '*':
                        toAdd = True
                        gearId = [i + 1, j]
                    if j > 0:
                        if input[i + 1][j - 1] == '*':
                            toAdd = True
                            gearId = [i + 1, j - 1]
                    if j < len(line) - 1:
                        if input[i + 1][j + 1] == '*':
                            toAdd = True
                            gearId = [i + 1, j + 1]
                if j == len(line) - 1 and toAdd: #Edge case when the number is at the end of the line
                    numbers.append([gearId, int(number)])
                    toAdd = False
                    number = ''
            else:
                if toAdd:
                    numbers.append([gearId, int(number)])
                    toAdd = False
                number = ''
    finalNumbers = []
    for i in range(len(numbers)):
        appears = 0
        numbersToMultiply = []
        for j in range(len(numbers)):
            if numbers[i][0] == numbers[j][0]:
                appears += 1
                numbersToMultiply.append(numbers[j][1])
        if appears == 2 and [numbersToMultiply[0], numbersToMultiply[1]] not in finalNumbers:
            finalNumbers.append([numbersToMultiply[0], numbersToMultiply[1]])
    answer = 0
    for number in finalNumbers:
        answer += number[0] * number[1]
    print(answer)
    
    
if __name__ == "__main__":
    main()