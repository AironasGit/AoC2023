def main():
    validDigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open('Day1/input.txt') as file:
        lines = file.readlines()
        values = []
        for line in lines:
            numbers = []
            for i, char in enumerate(line):
                for number, validDigit in enumerate(validDigits):
                   if validDigit in line[i:i+len(validDigit)]:
                       numbers.append(number + 1)
                if char.isdigit():
                    numbers.append(int(char))
            values.append(numbers[0] * 10 + numbers[-1])
        answer = sum(values)
        print(answer)


if __name__ == "__main__":
    main()