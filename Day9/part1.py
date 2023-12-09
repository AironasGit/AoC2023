def main():
    with open('Day9/input.txt') as file:
        lines = file.readlines()
    sequences = []
    for line in lines:
        sequences.append(list(map(int, line.split())))
    nextNumbers = []
    for sequence in sequences:
        subSequence = sequence
        newSequences = []
        while subSequence != [0] * (len(subSequence)):
            newSequence = []
            for i in range(0, len(subSequence) - 1):
                newSequence.append(subSequence[i + 1] - subSequence[i])
            newSequences.append(newSequence)
            subSequence = newSequence
        nextNumber = sequence[-1]
        for newSequence in newSequences:
            nextNumber += newSequence[-1]
        nextNumbers.append(nextNumber)
    answer = sum(nextNumbers)
    print(answer)


if __name__ == "__main__":
    main()