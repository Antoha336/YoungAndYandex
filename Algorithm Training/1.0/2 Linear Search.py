def task_a(numbers):
    answer = "YES"

    for i in range(len(numbers) - 1):
        if numbers[i + 1] <= numbers[i]:
            answer = "NO"
            # return answer

    return answer


def task_b():
    number_1 = int(input())
    number_2 = int(input())
    answer = "CONSTANT"
    flag = True
    while number_1 != -2 * 10 ** 9 and number_2 != -2 * 10 ** 9:
        if answer == "CONSTANT" and number_2 != number_1:
            if number_2 > number_1 and flag:
                answer = "ASCENDING"
            elif number_2 > number_1 and not flag:
                answer = "WEAKLY ASCENDING"
            elif number_2 < number_1 and flag:
                answer = "DESCENDING"
            else:
                answer = "WEAKLY DESCENDING"
        elif (answer == "ASCENDING" or answer == "DESCENDING") and number_2 == number_1:
            answer = "WEAKLY " + answer
        elif (answer == "ASCENDING" or answer == "WEAKLY ASCENDING") and number_2 != number_1:
            if number_2 < number_1:
                answer = "RANDOM"
        elif (answer == "DESCENDING" or answer == "WEAKLY DESCENDING") and number_2 != number_1:
            if number_2 > number_1:
                answer = "RANDOM"
        number_1 = number_2
        number_2 = int(input())
        flag = False

    return answer


def task_c(N, numbers, number):
    nearest_number = numbers[0]
    nearest_diff = abs(number - nearest_number)
    for i in range(1, N):
        if abs(numbers[i] - number) < nearest_diff:
            nearest_number = numbers[i]
            nearest_diff = abs(nearest_number - number)

    return nearest_number


def task_d(numbers):
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] > numbers[i + 1]:
            count += 1

    return count


def task_e(N, numbers):
    winner_distance = numbers[0]

    for i in range(1, N):
        if numbers[i] > winner_distance:
            winner_distance = numbers[i]

    vas = 0
    flag = False
    for i in range(N - 2):
        if not flag and numbers[i] == winner_distance:
            flag = True

        if flag and numbers[i + 1] % 10 == 5 and numbers[i + 2] < numbers[i + 1] and (
                vas == 0 or numbers[i + 1] > vas):
            if winner_distance == numbers[i + 1]:
                vas = winner_distance
            else:
                vas = numbers[i + 1]

    places = sorted(numbers, reverse=True)
    if vas != 0:
        vas = places.index(vas) + 1

    return vas


def task_f(N, numbers):
    def is_palindrome(array, start, end):
        size = end - start + 1
        ost = 0
        for i in range(start, size // 2 + start):
            if array[i] != array[end - ost]:
                return False
            ost += 1
        return True

    last_index = N - 1
    if is_palindrome(numbers, 0, last_index):
        return []

    answer = []
    for i in range(1, N):
        if is_palindrome(numbers, i, last_index):
            for j in range(i - 1, -1, -1):
                answer.append(numbers[j])
            return answer


def task_g(numbers):
    max_1 = numbers[0]
    max_2 = numbers[1]
    min_1 = numbers[0]
    min_2 = numbers[1]
    for i in range(2, len(numbers)):
        if numbers[i] > max_1:
            max_2 = max_1
            max_1 = numbers[i]
        elif numbers[i] > max_2:
            max_2 = numbers[i]
        if numbers[i] < min_1:
            min_2 = min_1
            min_1 = numbers[i]
        elif numbers[i] < min_2:
            min_2 = numbers[i]

    if max_1 * max_2 > min_1 * min_2:
        if max_1 <= max_2:
            summ = (max_1, max_2)
        else:
            summ = (max_2, max_1)
    else:
        if min_1 <= min_2:
            summ = (min_1, min_2)
        else:
            summ = (min_2, min_1)

    return summ


def task_h(numbers):
    sort_numbers = numbers[:3]
    sort_numbers.sort()
    maxx = sort_numbers[2]
    premaxx = sort_numbers[1]
    prepremax = sort_numbers[0]
    prepremin = sort_numbers[2]
    preminn = sort_numbers[1]
    minn = sort_numbers[0]

    for i in range(3, len(numbers)):
        if numbers[i] >= maxx:
            prepremax = premaxx
            premaxx = maxx
            maxx = numbers[i]
        elif numbers[i] >= premaxx:
            prepremax = premaxx
            premaxx = numbers[i]
        elif numbers[i] >= prepremax:
            prepremax = numbers[i]
        if minn >= numbers[i]:
            prepremin = preminn
            preminn = minn
            minn = numbers[i]
        elif preminn >= numbers[i]:
            prepremin = preminn
            preminn = numbers[i]
        elif prepremin >= numbers[i]:
            prepreminn = numbers[i]

    if len(numbers) == 3:
        return maxx, premaxx, prepremax
    else:
        base1 = max(minn * preminn * prepremin, maxx * premaxx * prepremax)
        base2 = max(minn * maxx * premaxx, minn * maxx * preminn)
        res = max(base1, base2)
        if minn * preminn * prepremin == res:
            return prepremin, preminn, minn
        elif maxx * premaxx * prepremax == res:
            return maxx, premaxx, prepremax
        elif minn * maxx * premaxx == res:
            return maxx, premaxx, minn
        else:
            return maxx, preminn, minn


def task_i(N, M, K):
    matrix = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        x, y = map(lambda x: int(x) - 1, input().split())
        matrix[x][y] = "*"

        for j in [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]:
            current_x = x + j[0]
            current_y = y + j[1]
            if (0 <= current_x <= N - 1) and (0 <= current_y <= M - 1):
                if type(matrix[current_x][current_y]) == int:
                    matrix[current_x][current_y] += 1

    return matrix


def task_j(N):
    def sr_arif(n_1, n_2):
        return (n_1 + n_2) / 2

    borders = [30.0, 4000.0]

    previous_number = int(input())

    for i in range(N - 1):
        number, mode = input().split()
        number = int(number)
        if (previous_number > number and mode == "closer") or (previous_number < number and mode == "further"):
            borders[1] = min(sr_arif(previous_number, number), borders[1])
        else:
            borders[0] = max(sr_arif(previous_number, number), borders[0])
        previous_number = number

    return borders


array = list(map(int, input().split()))

print(*task_h(array))