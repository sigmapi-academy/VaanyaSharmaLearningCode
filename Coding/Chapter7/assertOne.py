print('Use of assert statement')

def negativecheck(number:int):
    assert (number >= 0), "OOps.... Negative number"
    
    print(number * number)
    
print(negativecheck(100))
print(negativecheck(-350))