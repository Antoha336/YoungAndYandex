def task_a(numbers):
    return len(set(numbers))


def task_b(numbers_1, numbers_2):
    return sorted(set(numbers_1).intersection(set(numbers_2)))


def task_c(N, M):
    ann_cubes = set()
    bor_cubes = set()
    for i in range(N):
        ann_cubes.add(int(input()))

    for i in range(M):
        bor_cubes.add(int(input()))

    inter_cubes = ann_cubes.intersection(bor_cubes)
    left_ann_cubes = ann_cubes.difference(inter_cubes)
    left_bor_cubes = bor_cubes.difference(inter_cubes)

    return sorted(inter_cubes), sorted(left_ann_cubes), sorted(left_bor_cubes)


def task_d():
    words = []
    words_in_line = input().split()
    while words_in_line:
        words.extend(words_in_line)
        words_in_line = input().split()

    print(len(set(words)))


def task_e(x, y, z, number):
    buttons = {x, y, z}
    digits = set()
    while number > 0:
        digits.add(number % 10)
        number //= 10

    well = digits.difference(buttons)
    return len(well)


def task_f(string_1, string_2):
    gens_1 = {}
    for i in range(len(string_1) - 1):
        gen = string_1[i] + string_1[i + 1]
        if gen in gens_1:
            gens_1[gen] += 1
        else:
            gens_1[gen] = 1

    gens_2 = {}
    for i in range(len(string_2) - 1):
        gen = string_2[i] + string_2[i + 1]
        if gen in gens_2:
            gens_2[gen] += 1
        else:
            gens_2[gen] = 1

    gen_sum = 0
    for key in gens_2.keys():
        if key in gens_1:
            gen_sum += gens_1[key]

    return gen_sum


def task_h(N):
    temp = set()
    for i in range(N):
        x, y = map(int, input().split())
        temp.add(x)

    return len(temp)


def task_g(N):
    talks = []
    for i in range(N):
        a, b = map(int, input().split())
        talks.append([a, b])

    talks = sorted(talks, key=lambda x: (-x[0], x[1]))

    free = []
    to_insert = []
    for talk in talks:
        if talk[0] + talk[1] >= N:
            free.append([talk[0], talk[1]])
            talk[0] = 0
            talk[1] = 0
        elif talk[0] != 0 and talk[1] != 0:
            to_insert.append([talk[0], talk[1]])
            talk[0] = 0
            talk[1] = 0

    talks = sorted(talks, key=lambda x: (-x[0], x[1]))

    if not to_insert and free:
        i = 0
        trues = N - len(free)
        for talk in talks:
            if talk[0] + talk[1] == 0:
                talk[0] = free[i][0]
                talk[1] = free[i][1]
                i += 1

    elif not free and to_insert:
        i = 0
        trues = N - len(to_insert)
        for talk in talks:
            if talk[0] + talk[1] == 0:
                talk[0] = to_insert[i][0]
                talk[1] = to_insert[i][1]
                i += 1
                if talk[0] <= N - 1 - i and talk[1] >= i:
                    trues += 1

    else:
        trues = 0
        free_index, insert_index = len(free) - 1, 0

        for i in range(len(talks)):
            talk = talks[i]
            if talk[0] + talk[1] == 0:
                if insert_index < len(to_insert):
                    insert_talk = to_insert[insert_index]
                else:
                    talk[0] = free[free_index][0]
                    talk[1] = free[free_index][1]
                    free_index -= 1
                    continue

                if i >= insert_talk[1]:
                    talk[0] = insert_talk[0]
                    talk[1] = insert_talk[1]
                    insert_index += 1
                    if talk[0] <= N - 1 - i:
                        trues += 1
                else:
                    if free_index >= 0 and free_index + 1 + i >= insert_talk[1]:
                        for j in range(i, insert_talk[1]):
                            talks[j][0] = free[free_index][0]
                            talks[j][1] = free[free_index][1]
                            free_index -= 1
                        talks[insert_talk[1]][0] = insert_talk[0]
                        talks[insert_talk[1]][1] = insert_talk[1]
                        insert_index += 1
                        if talks[insert_talk[1]][0] <= N - 1 - insert_talk[1]:
                            trues += 1
                    else:
                        talk[0] = insert_talk[0]
                        talk[1] = insert_talk[1]
                        insert_index += 1

    return trues


def task_i(N):
    even_one = set()
    all_even = set()

    a = int(input())
    for j in range(a):
        s = input()
        even_one.add(s)
        all_even.add(s)

    for i in range(N - 1):
        a = int(input())
        w = set()
        for j in range(a):
            s = input()
            even_one.add(s)
            w.add(s)
        all_even = all_even.intersection(w)

    print(len(all_even))
    for i in all_even:
        print(i)

    print(len(even_one))
    for i in even_one:
        print(i)


x_1 = int(input())

task_i(x_1)
