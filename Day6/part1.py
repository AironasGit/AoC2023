def main():
    with open('Day6/input.txt') as file:
        lines = file.readlines()
    times = lines[0].split(':')[1].split()
    distances = lines[1].split(':')[1].split()
    races = [] #[[time, distance],...]
    for count in range(len(times)):
        races.append([int(times[count]), int(distances[count])])
    waysToWin = []
    for race in races:
        for i in range(race[0] + 1):
            distanceTraveled = i * (race[0] - i)
            if distanceTraveled > race[1]:
                waysToWin.append(race[0] - i - i + 1)
                break
    answer = 1
    for wayToWin in waysToWin:
        answer = answer*wayToWin
    print(answer)
    
    
if __name__ == "__main__":
    main()