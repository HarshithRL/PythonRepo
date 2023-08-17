#question 1
def list_command(N, C):
    list1 = []
    printed_list = []  # Initialize a variable to store printed lists
    for c in C:
        if c[0] == "insert":
            list1.insert(int(c[1]), int(c[2]))
        elif c[0] == "append":
            list1.append(int(c[1]))
        elif c[0] == "remove":
            list1.remove(int(c[1]))
        elif c[0] == "pop":
            list1.pop()
        elif c[0] == "sort":
            list1.sort()
        elif c[0] == "reverse":
            list1.reverse()
        elif c[0] == "print":
            printed_list.append(list1.copy())  # Store a copy of the list
    return list1, printed_list