def main():
    with open('Day4/input.txt') as file:
        temp = file.readlines()
    lines = []
    for line in temp:
        lines.append(line.strip())
    cards = [] # [copy count, [winningNumbers], [myNumbers]]
    for line in lines:
        numbers = line.split(': ')[1]
        winningNumbers = numbers.split(' | ')[0].split()
        myNumbers = numbers.split(' | ')[1].split()
        cards.append([1, winningNumbers, myNumbers])
    for i, card in enumerate(cards):
        count = 0
        for winningNumber in card[1]:
            for myNumber in card[2]:
                if winningNumber == myNumber:
                    count += 1
        for k in range(0, card[0]):
            for j in range(0, count):
                cards[i + 1 + j ][0] += 1
    answer = 0
    for card in cards:
        answer += card[0]
    print(answer)
    
    
if __name__ == "__main__":
    main()