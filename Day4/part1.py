def main():
    with open('Day4/input.txt') as file:
        temp = file.readlines()
    lines = []
    for line in temp:
        lines.append(line.strip())
    points = []
    for line in lines:
        numbers = line.split(': ')[1]
        winningNumbers = numbers.split(' | ')[0].split()
        myNumbers = numbers.split(' | ')[1].split()
        score = 0
        for winningNumber in winningNumbers:
            for myNumber in myNumbers:
                if winningNumber == myNumber:
                    if score == 0:
                        score = 1
                    else:
                        score = score * 2
        points.append(score)
    answer = sum(points)
    print(answer)


if __name__ == "__main__":
    main()