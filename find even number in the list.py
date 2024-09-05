def list_input():
    my_list = []

    item = int(input("How many item do you want to insert: "))

    for element in range(item):
        my_list.append(int(input(f'Item no {element + 1}: ')))
    print(f'Actual list is {my_list}')

    return my_list

def find_even_number(my_list):
    update_list = []

    for item in my_list:
        if item % 2 == 0:
            update_list.append(item)

    print(f'Even number in the actual list is : {update_list}')
    return update_list

find_even_number(list_input())