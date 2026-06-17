def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)  

A=int(input("Enter the first value: "))
B=int(input("Enter the second value: "))

print("The GCD is:", find_gcd(A, B))

