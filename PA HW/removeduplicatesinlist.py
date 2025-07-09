lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique = []
for i in lst:
 if i not in unique:
     unique.append(i)
print("List without duplicates:", unique)
