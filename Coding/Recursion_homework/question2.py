def list_sum(li):
    if not li:
        return 0
    return li[0] + list_sum(li[1:])

uinput = input("Enter a series of numbers separated by commas: ")

numbers = [int(i) for i in uinput.split(",")]

print("Sum:", list_sum(numbers))
