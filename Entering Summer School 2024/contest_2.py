"""
Задачи с второго тестового задания при поступлении в школу бэкенд-разработки 2024 года
https://www.notion.so/2e2e94ac2ab84bf69049e45d98680e89?pvs=4
"""


def task_a():
    def check_win(board):
        x_board = board["x"]
        y_board = board["y"]
        for _x in x_board.keys():
            if len(x_board[_x]) >= 5:
                for __x in x_board[_x]:
                    for i in range(1, 5):
                        if __x + i not in x_board[_x]:
                            break
                    else:
                        return True

        for _y in y_board.keys():
            if len(y_board[_y]) >= 5:
                for __y in y_board[_y]:
                    for i in range(1, 5):
                        if __y + i not in y_board[_y]:
                            break
                    else:
                        return True

        for _x in x_board:
            for _y in x_board[_x]:
                for i in range(1, 5):
                    if _x + i not in x_board or _y + i not in x_board[_x + i]:
                        break
                else:
                    return True

                for i in range(1, 5):
                    if _x + i not in x_board or _y - i not in x_board[_x + i]:
                        break
                else:
                    return True

        return False

    n = int(input())
    field_x = {"x": {}, "y": {}}
    field_o = {"x": {}, "y": {}}
    status = "Draw"
    for i in range(n):
        if i % 2 == 0:
            current_field = field_x
        else:
            current_field = field_o

        x, y = map(int, input().split())
        if x not in current_field["x"]:
            current_field["x"][x] = {y}
        else:
            current_field["x"][x].add(y)
        if y not in current_field["y"]:
            current_field["y"][y] = {x}
        else:
            current_field["y"][y].add(x)

        if check_win(current_field):
            if status == "Draw":
                status = "First" if i % 2 == 0 else "Second"
            else:
                return "Inattention"

    return status


def task_b():
    N, K = map(int, input().split())
    prices = list(map(int, input().split()))

    left, mid, right = N - K, 0, N - 1
    summa = 0
    days = ["0"] * N
    while right >= 0:
        mid = right
        min_number = prices[mid]
        min_index = mid
        while mid >= left:
            if prices[mid] < min_number:
                min_number = prices[mid]
                min_index = mid
            mid -= 1
        else:
            summa += min_number * (right - min_index + 1)
            days[min_index] = str(right - min_index + 1)
            right = min_index - 1
            left = right - K + 1
            if left < 0:
                left = 0

    with open("../output.txt", "w") as file:
        file.write(str(summa) + "\n")
        file.write(" ".join(days))


def task_c():
    def search(time_nodes, cost_nodes,
               visited_nodes,
               start, end, max_time,
               time=0, cost=0,
               results=None, ways=None):

        if time > max_time:
            if results is None:
                results = dict()
            return results

        if ways is None:
            ways = list()

        if start == end:
            if results is None:
                results = dict()
            results[(time, cost)] = tuple(ways)
            return results

        visited_nodes[start] = True

        for node in time_nodes.keys():
            if not visited_nodes[node] and node in time_nodes[start]:
                result = search(time_nodes, cost_nodes,
                                visited_nodes.copy(),
                                node, end, max_time,
                                time + time_nodes[start][node], cost + cost_nodes[start][node],
                                results, ways.copy() + [str(start) + str(node)])
                if results is None:
                    results = dict()
                results.update(result)

        return results

    N, M = map(int, input().split())

    time_nodes = dict()
    cost_nodes = dict()
    visited = dict()
    for i in range(N):
        time_nodes[i + 1] = dict()
        cost_nodes[i + 1] = dict()
        visited[i + 1] = False
    for i in range(M):
        node_1, node_2, time = map(int, input().split())
        time_nodes[node_1][node_2] = time
        time_nodes[node_2][node_1] = time
        cost_nodes[node_1][node_2] = 0
        cost_nodes[node_2][node_1] = 0

    K = int(input())
    deals = dict()
    for i in range(K):
        node_1, node_2, time, price = map(int, input().split())
        deals[(str(node_1) + str(node_2))] = i + 1
        time_nodes[node_1][node_2] = time
        time_nodes[node_2][node_1] = time
        cost_nodes[node_1][node_2] = price
        cost_nodes[node_2][node_1] = price

    P = int(input())
    for i in range(P):
        node_1, node_2, time = map(int, input().split())
        findings = search(time_nodes, cost_nodes, visited, node_1, node_2, time)
        own_way = min(findings, key=lambda x: (x[1]))

    deals_to_agree = list()
    for way in findings[own_way]:
        if way in deals:
            deals_to_agree.append(str(deals[way]))

    print(len(deals_to_agree))
    print(" ".join(sorted(deals_to_agree)))


task_c()
