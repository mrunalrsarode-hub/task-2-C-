# Swap first and last element

lst = [10, 20, 30, 40, 50]

temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp

print("After swapping:", lst)