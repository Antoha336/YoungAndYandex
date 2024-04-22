from itertools import permutations


def task_a():
    N = int(input())
    t_shirts = list(map(int, input().split()))
    M = int(input())
    pants = list(map(int, input().split()))

    i = 0
    j = 0
    min_sum = abs(t_shirts[i] - pants[j])
    t_shirt = t_shirts[i]
    pant = pants[j]
    while i < N and j < M:
        if abs(t_shirts[i] - pants[j]) < min_sum:
            min_sum = abs(t_shirts[i] - pants[j])
            t_shirt = t_shirts[i]
            pant = pants[j]

        if t_shirts[i] > pants[j]:
            j += 1
        else:
            i += 1

    return t_shirt, pant


def task_b():
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    count = 0
    list_prefixes = [0]
    set_prefixes = {0}
    for i in range(N):
        list_prefixes.append(numbers[i] + list_prefixes[i])
        set_prefixes.add(numbers[i] + list_prefixes[i])
        if list_prefixes[i + 1] - K in set_prefixes:
            count += 1

    return count


def task_c():
    N = int(input())
    x, y = map(int, input().split())
    hills = [y]
    left_prefixes = [0]
    for i in range(1, N):
        x, y = map(int, input().split())
        hills.append(y)
        height = hills[i] - hills[i - 1]
        if height < 0:
            height = 0
        left_prefixes.append(left_prefixes[i - 1] + height)

    right_prefixes = [0]
    for i in range(1, N):
        height = hills[N - i - 1] - hills[N - i]
        if height < 0:
            height = 0
        right_prefixes.append(right_prefixes[i - 1] + height)

    M = int(input())
    for i in range(M):
        start, end = map(lambda x: int(x) - 1, input().split())
        if start <= end:
            print(left_prefixes[end] - left_prefixes[start])
        else:
            print(right_prefixes[start] - right_prefixes[end])


def task_d():
    n, r = map(int, input().split())
    distances = list(map(int, input().split()))

    count = 0
    left = 0
    right = 1
    while left < n and right < n:
        if distances[right] - distances[left] > r:
            count += n - right
            left += 1
        else:
            right += 1

    print(count)


def task_e():
    N, K = map(int, input().split())
    trees = list(map(int, input().split()))
    trees_in_line = {trees[0]: 1}
    answer = (0, N)

    left = 0
    right = 0
    operation = "r"
    while left < N and (operation == "r" and right + 1 < N or operation == "l") and right < N:
        if operation == "r":
            right += 1
            if trees[right] not in trees_in_line:
                trees_in_line[trees[right]] = 1
                operation = "r"
            else:
                trees_in_line[trees[right]] += 1
                if trees[right] == trees[left]:
                    operation = "l"
        elif operation == "l":
            trees_in_line[trees[left]] -= 1
            left += 1
            if trees[left] == trees[left + 1] and left != right:
                operation = "l"
            else:
                operation = "r"

        if len(trees_in_line) == K:
            answer = min((left, right), answer, key=lambda x: (x[1] - x[0]))
            if right - left + 1 != K:
                if trees_in_line[trees[left]] > 1 or operation == "l":
                    operation = "l"
                else:
                    operation = "r"
            else:
                break

    return answer[0] + 1, answer[1] + 1


def task_f():
    n = int(input())
    classes = list(map(int, input().split()))
    m = int(input())
    conditioners = dict()
    for i in range(m):
        power, cost = map(int, input().split())
        if cost not in conditioners:
            conditioners[cost] = power
        else:
            if power > conditioners[cost]:
                conditioners[cost] = power

    sorted_costs = sorted(conditioners.keys())
    sorted_powers = sorted(classes)

    left = 0
    right = 0
    sum_cost = 0
    while left < m and right < n:
        cond_power = conditioners[sorted_costs[left]]
        class_power = sorted_powers[right]
        if cond_power >= class_power:
            sum_cost += sorted_costs[left]
            right += 1
        else:
            left += 1

    return sum_cost


def task_g():
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))

    combs = list()
    sorted_cards = sorted(cards)
    left = 0
    right = 0
    comb = 0
    while left < n and right < n:
        if sorted_cards[right] / sorted_cards[left] <= k:
            if len(combs) - 1 != comb:
                combs.append([sorted_cards[right]])
            else:
                combs[comb].append(sorted_cards[right])
            right += 1
        else:
            left += 1
            right = left
            comb += 1

    combinations = set()
    for combination in combs:
        combinations.update(set(permutations(combination, 3)))

    return len(combinations)


def task_h():
    n, k = map(int, input().split())
    line = input()

    left = 0
    right = 0
    max_len = 0
    char_count = {"0": 0}
    while left < n and right < n:
        left_char = line[left]
        right_char = line[right]
        if (right_char in char_count and char_count[right_char] > k) or (max(char_count.values()) > k):
            char_count[left_char] -= 1
            left += 1
        else:
            right += 1
            if right_char not in char_count:
                char_count[right_char] = 1
            else:
                char_count[right_char] += 1
        print(char_count)


    return max_len


print(task_h())
