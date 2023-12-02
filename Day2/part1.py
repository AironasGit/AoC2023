def main():
    bag = (12, 13, 14) #(RED, GREEN, BLUE)
    with open('Day2/input.txt') as file:
        lines = file.readlines()
        validGames = []
        for line in lines:
            validSubsets = 0
            id = int(line.split(':')[0].split(' ')[1])
            subsets = line.split(':')[1].split(';')
            for subset in subsets:
                red = 0
                green = 0
                blue = 0
                cubes = subset.split(',')
                for cube in cubes:
                    if 'red' in cube:
                        red += int(cube.split('red')[0])
                    if 'green' in cube:
                        green += int(cube.split('green')[0])
                    if 'blue' in cube:
                        blue += int(cube.split('blue')[0])
                if red <= bag[0] and green <= bag[1] and blue <= bag[2]:
                    validSubsets += 1
            if validSubsets == len(subsets):
                validGames.append(id)
        answer = sum(validGames)
        print(answer)


if __name__ == "__main__":
    main()