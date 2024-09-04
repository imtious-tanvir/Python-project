def sum(my_list):
    total = 0
    for item in my_list:
        total += item
    print(f'Sum of list elements is {total}')
    return total

def list_input():
    my_list = []

    item = int(input("How many item do you want to insert: "))

    for element in range(item):
        my_list.append(int(input(f'Item no {element + 1}: ')))
    print(f'My list is {my_list}')
    return my_list

sum(list_input())