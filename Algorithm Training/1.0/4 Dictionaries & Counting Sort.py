def task_a():
    N = int(input())
    word_list_1 = {}
    word_list_2 = {}
    for i in range(N):
        word_1, word_2 = input().split()
        word_list_2[word_1] = word_2
        word_list_2[word_2] = word_1

    word = input()
    if word in word_list_1:
        return word_list_1[word]
    else:
        return word_list_2[word]


def task_b():
    words = list()
    with open("../../input.txt", "r") as file:
        line = file.readline()
        while line:
            words.extend(line.split())
            line = file.readline()
    words_dict = dict()
    answer = []
    for word in words:
        if word not in words_dict:
            words_dict[word] = 0
        else:
            words_dict[word] += 1
        answer.append(str(words_dict[word]))

    return " ".join(answer)


def task_c():
    words = dict()
    max_num = 0
    min_word = ""
    with open("../../input.txt", "r") as file:
        line = file.readline()
        while line:
            for word in line.split():
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1

                if words[word] > max_num:
                    max_num = words[word]
                    min_word = word
                elif words[word] == max_num and word < min_word:
                    min_word = word
            line = file.readline()

    return min_word


def task_d():
    n = int(input())
    keys = dict()
    keyss = list(map(int, input().split()))
    for i in range(n):
        keys[i + 1] = keyss[i]

    k = int(input())
    presses = list(map(int, input().split()))
    for i in presses:
        keys[i] -= 1

    for key in keys.keys():
        if keys[key] < 0:
            print("YES")
        else:
            print("NO")


def task_e():
    N = int(input())
    wides = dict()
    for i in range(N):
        wide, height = map(int, input().split())
        if wide not in wides:
            wides[wide] = [height]
        else:
            wides[wide].append(height)

    max_height = 0
    for wide in wides:
        max_height += max(wides[wide])

    return max_height


def task_f():
    clients = dict()
    with open("../../input.txt", "r") as file:
        line = file.readline()
        while line:
            name, product, amount = line.split()
            amount = int(amount)
            if name not in clients:
                clients[name] = {product: amount}
            else:
                if product not in clients[name]:
                    clients[name][product] = amount
                else:
                    clients[name][product] += amount
            line = file.readline()

    for client in sorted(clients.keys()):
        print(f"{client}:")
        for product in sorted(clients[client].keys()):
            print(product, clients[client][product])


def task_g():
    clients = dict()
    with open("../../input.txt", "r") as file:
        line = file.readline()
        while line:
            line = line.split()
            size = len(line)
            if size == 2:
                command = line[0]
                if command == "INCOME":
                    percent = int(line[1])
                    for client in clients.keys():
                        if clients[client] > 0:
                            clients[client] += int(clients[client] * percent / 100)
                else:
                    name = line[1]
                    if name not in clients:
                        print("ERROR")
                    else:
                        print(clients[name])
            elif size == 3:
                command = line[0]
                name = line[1]
                amount = int(line[2])
                if command == "DEPOSIT":
                    if name not in clients:
                        clients[name] = amount
                    else:
                        clients[name] += amount
                if command == "WITHDRAW":
                    if name not in clients:
                        clients[name] = -amount
                    else:
                        clients[name] -= amount
            else:
                name_1, name_2 = line[1], line[2]
                amount = int(line[3])
                if name_1 not in clients:
                    clients[name_1] = -amount
                else:
                    clients[name_1] -= amount

                if name_2 not in clients:
                    clients[name_2] = amount
                else:
                    clients[name_2] += amount

            line = file.readline()


def task_h():
    word_length, line_length = map(int, input().split())
    word = input()

    word_chars = dict()
    for char in word:
        if char not in word_chars:
            word_chars[char] = 1
        else:
            word_chars[char] += 1

    line = input()
    line_chars = dict()
    current_length = 0
    count = 0
    for i in range(line_length):
        char = line[i]
        if current_length >= word_length:
            current_char = line[i - word_length]
            line_chars[current_char] -= 1
            current_length -= 1
            if line_chars[current_char] == 0:
                line_chars.pop(current_char)

        if char not in line_chars:
            line_chars[char] = 1
        else:
            line_chars[char] += 1
        current_length += 1

        if line_chars == word_chars:
            count += 1

    return count


def task_i():
    N = int(input())
    dictionary = dict()
    for i in range(N):
        word = input()
        if word.lower() not in dictionary:
            dictionary[word.lower()] = [word]
        else:
            dictionary[word.lower()].append(word)

    line = input().split()
    mistakes = 0
    for word in line:
        word_1 = set()
        word_2 = set()
        for i in word:
            word_1.add(i.upper())
            word_2.add(i)
        emphasis = word_1.intersection(word_2)
        emphasises = len(emphasis)

        if emphasises == 0 or emphasises > 1 or (word.lower() in dictionary and word not in dictionary[word.lower()]):
            mistakes += 1
        elif emphasises == 1 and word.count(list(emphasis)[0]) != 1:
            mistakes += 1

    return mistakes


def task_k():
    def clear_line(line):
        answer = list()
        for char in line:
            if char.isalpha() or char.isdigit() or char == "_":
                answer.append(char)
            else:
                answer.append(" ")

        return "".join(answer).split()

    def get_identifiers(words: list, keywords: set, is_nums: bool):
        answer = list()
        for word in words:
            if not word.isdigit() and (is_nums or (not is_nums and not word[0].isdigit())) and word not in keywords:
                answer.append(word)

        return answer

    def read_line(file, is_register):
        if is_register:
            return file.readline()
        else:
            return file.readline().lower()

    words_count = dict()
    keywords = set()
    with open("../../input.txt", "r") as file:
        line = file.readline()
        n, C, D = line.split()
        n, C, D = int(n), C == "yes", D == "yes"

        max_num = 0
        max_word = ""

        line = read_line(file, C)
        for i in range(int(n)):
            keywords.add(line.strip())
            line = read_line(file, C)

        while line:
            for word in get_identifiers(clear_line(line), keywords, D):
                if word not in words_count:
                    words_count[word] = 1
                else:
                    words_count[word] += 1

                if words_count[word] > max_num:
                    max_num = words_count[word]
                    max_word = word
            line = read_line(file, C)

    return max_word


print(task_k())
