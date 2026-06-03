# Sum of non-negative numbers

lst = [1, 4, -5, -20, 10]

total = 0

for i in lst:
    if i >= 0:
        total = total + i

print("Sum =", total)