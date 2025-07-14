userinput = input("Enter numbers: ")
arr = userinput.split()
k = int(input("Enter how many positions to rotate left: "))
k = k % len(arr)
rotate = arr[k:] + arr[:k]
print("Left Rotate list:", rotate)
