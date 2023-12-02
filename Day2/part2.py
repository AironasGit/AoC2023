def main():
    with open('Day2/input.txt') as file:
        lines = file.readlines()
        games = []
        for line in lines:
            red = 0
            green = 0
            blue = 0
            subsets = line.split(':')[1].split(';')
            for subset in subsets:
                cubes = subset.split(',')
                for cube in cubes:
                    if 'red' in cube:
                        newRed = int(cube.split('red')[0])
                        if red < newRed:
                            red = newRed
                    if 'green' in cube:
                        newGreen = int(cube.split('green')[0])
                        if green < newGreen:
                            green = newGreen
                    if 'blue' in cube:
                        newBlue = int(cube.split('blue')[0])
                        if blue < newBlue:
                            blue = newBlue
            games.append(red * green * blue)
        answer = sum(games)
        print(answer)


if __name__ == "__main__":
    main()