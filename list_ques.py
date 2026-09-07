# Problem: Given the list numbers = [10, 20, 30, 40, 50, 60, 70, 80], perform the following:

# Extract a sublist containing [30, 40, 50].

# Reverse the entire list using slicing.

# Replace the last two elements with [90, 100].

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
sublist= numbers[2:5]
print(sublist)
reverse =  numbers[::-1]
print(reverse)
replace = numbers[-2:]
print(replace)
