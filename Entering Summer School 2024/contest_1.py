"""
Задачи с первого тестового задания при поступлении в школу бэкенд-разработки 2024 года
https://www.notion.so/c8b8e22e70af4e63bd9f64b1d8170550?pvs=4
"""

from string import ascii_uppercase, ascii_lowercase


def task_a():
    nick = input()
    is_upper = False
    is_lower = False

    if len(nick) < 8:
        return "NO"

    for i in range(0, 10):
        if str(i) in nick:
            break
    else:
        return "NO"

    for i in range(len(ascii_uppercase)):
        if ascii_uppercase[i] in nick:
            is_upper = True
        if ascii_lowercase[i] in nick:
            is_lower = True
        if is_upper and is_lower:
            break
    else:
        return "NO"

    return "YES"


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class List:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last


def task_b():
    line = input()
    input_line = input()

    right = 0
    new_line = list()

    while right < len(input_line):
        if input_line[right] == "<":
            right += 1
            command = list()
            while input_line[right] != ">":
                command.append(input_line[right])
                right += 1
            else:
                right += 1
            command = "".join(command)
            new_line.append(command)
        else:
            new_line.append(input_line[right])
            right += 1

    pointer = Node(None)
    llist = List(first=pointer, last=pointer)
    for i in range(0, len(new_line)):
        command = new_line[i]
        if command not in {"left", "right", "bspace", "delete"}:
            new_node = Node(new_line[i])
            if pointer == llist.first:
                # List.first -> new_node
                llist.first = new_node
                # new_node <- pointer
                pointer.prev_node = new_node
                # new_node -> pointer
                new_node.next_node = pointer
            else:
                # prev -> new_node
                pointer.prev_node.next_node = new_node
                # new -> pointer
                new_node.next_node = pointer
                # prev <- new_node
                new_node.prev_node = pointer.prev_node
                # new_node <- pointer
                pointer.prev_node = new_node
        else:
            if command == "left" and pointer != llist.first:
                if pointer == llist.last:
                    if pointer.prev_node.prev_node:
                        # pointer -> prev and prev_prev <- pointer
                        pointer.next_node = pointer.prev_node
                        pointer.prev_node = pointer.prev_node.prev_node
                        # pointer <- prev and prev_prev -> pointer
                        pointer.next_node.prev_node = pointer
                        pointer.prev_node.next_node = pointer
                        # prev -> None
                        pointer.next_node.next_node = None
                        llist.last = pointer.next_node
                    else:
                        # pointer -> prev and prev -> pointer
                        pointer.next_node = pointer.prev_node
                        pointer.next_node.prev_node = pointer
                        # None <- pointer and prev -> None
                        pointer.prev_node = None
                        pointer.next_node.next_node = None
                        llist.first = pointer
                        llist.last = pointer.next_node
                elif pointer.prev_node == llist.first:
                    if pointer.next_node:
                        # prev -> next and next <- prev
                        pointer.prev_node.next_node = pointer.next_node
                        pointer.next_node.prev_node = pointer.prev_node
                        # None <- pointer and pointer -> prev
                        pointer.next_node = pointer.prev_node
                        pointer.next_node.prev_node = pointer
                        # None <- pointer
                        pointer.prev_node = None
                    else:
                        # pointer -> prev
                        pointer.next_node = pointer.prev_node
                        # prev -> None and pointer <- prev
                        pointer.next_node.next_node = None
                        pointer.next_node.prev_node = pointer

                    llist.first = pointer
                else:
                    pointer.prev_node.next_node = pointer.next_node
                    pointer.next_node.prev_node = pointer.prev_node
                    # pointer -> prev and prev_prev <- pointer
                    pointer.next_node = pointer.prev_node
                    pointer.prev_node = pointer.prev_node.prev_node
                    # pointer <- prev and prev_prev -> pointer
                    pointer.prev_node.next_node.prev_node = pointer
                    pointer.prev_node.next_node = pointer
            elif command == "right" and pointer != llist.last:
                if pointer.next_node == llist.last:
                    if pointer != llist.first:
                        # next -> pointer and prev <- next
                        pointer.next_node.next_node = pointer
                        pointer.next_node.prev_node = pointer.prev_node
                        # prev -> next and next <- pointer
                        pointer.prev_node.next_node = pointer.next_node
                        pointer.prev_node = pointer.next_node
                        # pointer -> None
                        pointer.next_node = None
                    else:
                        pointer.next_node.next_node = pointer
                        pointer.next_node.prev_node = None
                        pointer.prev_node = pointer.next_node
                        pointer.next_node = None
                        llist.first = pointer.prev_node
                    llist.last = pointer

                elif pointer == llist.first:
                    # next <- pointer and None <- next
                    pointer.prev_node = pointer.next_node
                    pointer.prev_node.prev_node = None
                    # pointer -> next_next and pointer <- next_next
                    pointer.next_node.next_node.prev_node = pointer
                    pointer.next_node = pointer.next_node.next_node
                    # next -> pointer
                    pointer.prev_node.next_node = pointer

                    llist.first = pointer.prev_node
                else:
                    # prev -> next and prev <- next
                    pointer.prev_node.next_node = pointer.next_node
                    pointer.next_node.prev_node = pointer.prev_node
                    # next <- pointer and pointer -> next_next
                    pointer.prev_node = pointer.next_node
                    pointer.next_node = pointer.next_node.next_node
                    # prev -> pointer and pointer <- next
                    pointer.prev_node.next_node = pointer
                    pointer.next_node.prev_node = pointer
            elif command == "bspace" and pointer != llist.first:
                if pointer.prev_node == llist.first:
                    # prev -> None and None <- pointer
                    pointer.prev_node.next_node = None
                    pointer.prev_node = None
                    # List.first -> pointer
                    llist.first = pointer
                else:
                    # prev_prev <- pointer
                    pointer.prev_node = pointer.prev_node.prev_node
                    # prev -> None and None <- prev
                    pointer.prev_node.next_node.next_node = None
                    pointer.prev_node.next_node.prev_node = None
                    # prev_prev -> pointer
                    pointer.prev_node.next_node = pointer
            elif command == "delete" and pointer != llist.last:
                if pointer.next_node == llist.last:
                    # None <- next and pointer -> None
                    pointer.next_node.prev_node = None
                    pointer.next_node = None
                    # List.last -> pointer
                    llist.last = pointer
                else:
                    if pointer.next_node.next_node:
                        # None <- next and pointer -> next_next
                        pointer.next_node.prev_node = None
                        pointer.next_node = pointer.next_node.next_node
                        # next -> None and pointer <- next_next
                        pointer.next_node.prev_node.next_node = None
                        pointer.next_node.prev_node = pointer
                    else:
                        pointer.next_node.prev_node = None
                        pointer.next_node = None
                        llist.last = pointer

    node = llist.first
    final_string = list()
    while node is not None:
        if node.value:
            final_string.append(node.value)
        node = node.next_node
    final_string = "".join(final_string)

    if final_string == line:
        return "Yes"
    else:
        return "No"


print(task_b())
