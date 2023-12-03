def main():
    with open('Day3/input.txt') as file:
        lines = file.readlines()
        input = []
        for line in lines:
            input.append(line.strip())
        numbers = []
        for i, line in enumerate(input):
            number = ''
            toAdd = False
            for j, symbol in enumerate(line):
                if symbol.isdigit():
                    number += symbol
                    if i > 0:
                        if not input[i - 1][j].isdigit() and input[i - 1][j] != '.':
                            toAdd = True
                        if j > 0:
                            if not input[i - 1][j - 1].isdigit() and input[i - 1][j - 1] != '.':
                                toAdd = True
                        if j < len(line) - 1:
                            if not input[i - 1][j + 1].isdigit() and input[i - 1][j + 1] != '.':
                                toAdd = True
                    if j > 0:
                        if not input[i][j - 1].isdigit() and input[i][j - 1] != '.':
                            toAdd = True
                    if j < len(line) - 1:
                        if not input[i][j + 1].isdigit() and input[i][j + 1] != '.':
                            toAdd = True
                    if i < len(input) - 1:
                        if not input[i + 1][j].isdigit() and input[i + 1][j] != '.':
                            toAdd = True
                        if j > 0:
                            if not input[i + 1][j - 1].isdigit() and input[i + 1][j - 1] != '.':
                                toAdd = True
                        if j < len(line) - 1:
                            if not input[i + 1][j + 1].isdigit() and input[i + 1][j + 1] != '.':
                                toAdd = True
                    if j == len(line) - 1 and toAdd: #Edge case when the number is at the end of the line
                        numbers.append(int(number))
                        toAdd = False
                        number = ''
                else:
                    if toAdd:
                        numbers.append(int(number))
                        toAdd = False
                    number = ''
        answer = sum(numbers)
        print(answer)


if __name__ == "__main__":
    main()