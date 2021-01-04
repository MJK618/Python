#CS Dojo Problem 1


def helper(string,k):
    if k == 0:
        return 1
    else:
        s  = len(string) - k
        if string[s] == 0:
            return 0
        else:
            result = helper(string,k-1)
            if (k>=2 and int(string[s:s+2]) <= 26):
                            result += helper(string, k - 2)
    return result


def num_ways(string):
    return helper(string,len(string))

a='1111'
print(num_ways(a))


        
