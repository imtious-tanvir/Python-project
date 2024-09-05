def list_input_1():
    my_list = []

    item = int(input("How many item do you want to insert in list-1: "))

    for element in range(item):
        my_list.append(int(input(f'Item no {element + 1}: ')))

    return my_list


def list_input_2():
    my_list = []

    item = int(input("How many item do you want to insert in list-2: "))

    for element in range(item):
        my_list.append(int(input(f'Item no {element + 1}: ')))

    return my_list


def marge_list(list_1, list_2):
    final_list = list_1 + list_2

    print(f'Final list is: {final_list}')
    return final_list

marge_list(list_input_1(), list_input_2())