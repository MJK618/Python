#K Closest points to the Origin
import math


points = [(-2,4),(1,4),(3,5),(0,-5)]
dis = {}
def find_distance(list):
    for i in range(len(points)):
        s = (points[i][0])**2  + (points[i][1])**2
        s2 = math.sqrt(s)
        
        dis.append(s2)
    return dis

print(find_distance(points))
dis.sort()
k = int(input("Enter the number of closest "))

for i in range(k):
    print(dis[i])

    
