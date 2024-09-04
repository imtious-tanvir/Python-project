def list_input():
    my_list = []

    item = int(input("How many item do you want to insert: "))

    for element in range(item):
        my_list.append(int(input(f'Item no {element + 1}: ')))
    print(f'Actual list is {my_list}')

    return my_list

def reverse_list(my_list):

    reverse_list = my_list[::-1]

    print(f'Reverse list is {reverse_list}')
    return reverse_list

reverse_list(list_input())