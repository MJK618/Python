#Adding 1 in a number reprsented by a list

list_x=[1,5,4,13]
result = [0]*(len(list_x)-1)
def add_one(list_x):
    carry = 1
    
    for i in range(len(list_x)-1, 0):
        total = list_x[i] + carry
        if total == 10:
            carry = 1
        else:
            carry = 0
        result.append(i,(total%10))
        print(result)
    if carry == 1:
        result = [0]*len(list_x)
        result.insert(0,1)
            
    return result


print(add_one(list_x))
