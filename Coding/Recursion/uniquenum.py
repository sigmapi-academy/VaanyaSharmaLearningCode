def checkunique(n,d=None):
    d1=n%10
    if n>0:
        if d == d1:
            return False
        else:
            n = n//10
            return checkunique(n,d)
    else:
        return True
   
def isunique(n):
    d=n%10
    if n>9:
        n = n //10
        if not checkunique(n,d):
            return False
        else:
            return isunique(n//10)
    else:
        return True      
       
num=int(input("Enter the number you want to check: "))
if isunique(num):
    print("Your number is unique.")
else:
    print("Your number is not unique.")
 