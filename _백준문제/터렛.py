import math

#n = int(input())
x_1, y_1, r_1, x_2, y_2, r_2 = list(map(int, input().split()))

def dis(a,b,c,d):
    #(a-c)**2+(b-d)**2
    rst = int(math.sqrt((a**2-2*a*c+c**2) + (b**2-2*b*d+d**2)))
    return rst

def case(d, r1, r2):
    if r1> d or r2 > d:
        return 0
    else : 
        if d == r1+r2:
            return 1
        elif d > r1+r2:
            return 0
        elif d < r1+r2 :
            return 2
        else :
            return -1
        
distance = dis(x_1, y_1, x_2, y_2)
nice = case(distance, r_1, r_2)
print(nice)