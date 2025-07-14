user_input = input("Enter numbers: ")
input_list = user_input.split()
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
print("List without duplicates:", unique_list)
