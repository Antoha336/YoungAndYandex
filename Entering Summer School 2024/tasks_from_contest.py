"""
Случайные задачи из тестовых заданий при поступлении в летнюю школу
"""


def task_a():
    array = list(map(int, input().split()))
    series = list()
    deleted = 0
    i = 0
    size = len(array)
    while i < size:
        number = array[i]
        end = i
        for j in range(i + 1, size):
            end = j - 1
            if number != array[j]:
                break
        else:
            if end + 1 < size:
                end += 1

        border = [i, end]
        series.append(border)
        i = end + 1

    i = 0
    size = len(series)
    while i < size:
        new_i = i
        interval = series[i]
        if interval[1] - interval[0] >= 2:
            if 0 < i < size - 1:
                previous_series = series[i - 1]
                next_series = series[i + 1]
                if array[previous_series[0]] == array[next_series[0]]:
                    previous_series[1] += next_series[1] - next_series[0] + 1
                    series.pop(i + 1)
                    size -= 1
                    new_i = i - 2
            series.pop(i)
            deleted += interval[1] - interval[0] + 1
            size -= 1
            new_i -= 1
        new_i += 1

        i = new_i

    return deleted


def task_b():
    n = int(input())
    combs = {}
    for i in range(n):
        command = input().split()
        if len(command) == 3:
            if command[2] not in combs:
                combs[command[2]] = int(command[1])
            else:
                combs[command[2]] += int(command[1])
        else:
            max_comb = command[1]
            prefix = command[1]
            max_num = 0
            for key in combs.keys():
                if key.find(prefix, 0, len(prefix)) == 0:
                    if combs[key] > max_num:
                        max_num = combs[key]
                        max_comb = key
                    elif combs[key] == max_num and max_comb > key:
                        max_comb = key
            print(max_comb)


def task_3():
    N, S, T = map(int, input().split())
    array = list(map(int, input().split()))

    times = dict()
    for i in array:
        if i not in times:
            times[i] = 1
        else:
            times[i] += 1

    cells = {}
    served = {}
    current_visitors = 0
    for i in range(max(times) + 1):
        if i in cells:
            current_visitors -= cells[i]
            cells.pop(i)

        if i in times:
            if current_visitors < S:
                if S - current_visitors >= times[i]:
                    if i + T not in cells:
                        cells[i + T] = times[i]
                    else:
                        cells[i + T] += times[i]
                    served[i] = times[i]
                    current_visitors += times[i]
                else:
                    if i + T not in cells:
                        cells[i + T] = S - current_visitors
                    else:
                        cells[i + T] += S - current_visitors
                    served[i] = S - current_visitors
                    current_visitors += S - current_visitors

    for i in array:
        if i in served and served[i] != 0:
            print("YES")
            served[i] -= 1
        else:
            print("NO")


def task_4():
    def search(current_tower, towers, end_location):
        relations = {current_tower: []}
        current_x, current_y, current_r = current_tower[0], current_tower[1], towers[current_tower]
        towers.pop(current_tower)
        for tower in towers:
            x, y, r = tower[0], tower[1], towers[tower]
            if abs(x - current_x) - 1 <= current_r + r and abs(y - current_y) - 1 <= current_r + r:
                relations[current_tower].append(tower)
                if tower == end_location:
                    return 1

        print(relations)
        for tower in relations[current_tower]:
            return search(tower, towers, end_location)

        return 0

    N = int(input())
    towers = dict()
    for i in range(N):
        x, y, r = map(int, input().split())
        towers[(x, y)] = r
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    start_location = 0
    end_location = 0
    for tower in towers.keys():
        x, y = tower
        if abs(x - start_x) <= towers[tower] and abs(y - start_y) <= towers[tower]:
            start_location = tower
        if abs(x - end_x) <= towers[tower] and abs(y - end_y) <= towers[tower]:
            end_location = tower

    if start_location == 0 or end_location == 0:
        return 0

    return search(start_location, towers, end_location)


print(task_4())
