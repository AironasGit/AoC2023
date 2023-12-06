def main():
    with open('Day6/input.txt') as file:
        lines = file.readlines()
    times = lines[0].split(':')[1].split()
    distances = lines[1].split(':')[1].split()
    time = ''
    distance = ''
    for count in range(len(times)):
        time += times[count]
        distance += distances[count]
    race = [int(time), int(distance)] #[[time, distance],...]
    count = 0
    for i in range(race[0] + 1):
        distanceTraveled = i * (race[0] - i)
        if distanceTraveled > race[1]:
            count = i
            break
    answer = race[0] - count - count + 1
    print(answer)
    
    
if __name__ == "__main__":
    main()