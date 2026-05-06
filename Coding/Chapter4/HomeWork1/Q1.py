# 	1. Reverse a List Using Slicing
# Write a program to reverse a list using list slicing without using the reverse() function.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

li = eval(input('Enter the list elements by separating comma: '))

print(li)
li = li[::-1]
print(li)