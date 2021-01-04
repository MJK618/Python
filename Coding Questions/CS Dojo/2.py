#Steps Problem
import array


#Top to Bottom Approach

def num_ways(n):
    if n==0 or n==1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)


#Bottom Up Approach

nums=[] 
def num_ways_bottom_up(n):
    if n == 0 or n==1:
        return 1
    else:
        nums.append(1)
        nums.append(1)
        for i in range(2,n+1):
            val = nums[i-1] + nums[i-2]
            nums.append(val) 
    return nums[n]


#The special case
def num_ways_X(n):
    if n == 0:
        return 1
    else:
        total = 0
        for i in {1, 3, 5}:
            if n-i >=0:
                total += num_ways_X(n-i)
    return total


def num_ways_X_bottom_up(n):
    if n == 0:
        return 1
    else:
        nums_x=[]
        nums_x.append(1)
        for i in range(1,n+1):
            total_x = 0
            for j in {1, 3, 5}:
                if i-j >= 0:
                    total_x += nums_x[i-j]
            nums_x.append(total_x) 
    return nums_x[n]




print(num_ways(37))
print(num_ways_bottom_up(37))
print(num_ways_X(37))
print(num_ways_X_bottom_up(37))
    
 
