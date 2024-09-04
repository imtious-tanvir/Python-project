def remove_dublicate(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

item = int(input("How many item do you want to insert: "))

input_list = []

for element in range(item):
    input_list.append(int(input(f'Item no {element+1}: ' )))

final_list = remove_dublicate(input_list)

print(f'Final list is {final_list}')