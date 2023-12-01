def main():
    with open('Day1/input.txt') as file:
        lines = file.readlines()
        values = []
        for line in lines:
            numbers = []
            for char in line:
                if char.isdigit():
                    numbers.append(int(char))
            values.append(numbers[0] * 10 + numbers[-1])
        answer = sum(values)
        print(answer)


if __name__ == "__main__":
    main()