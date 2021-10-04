D = [0]*100

def DP(x):
    c = 0


    if x//5 ==0 :
        return D[x]
        c += 1 
    elif x//3 == 0 :
        return D[x]
        c += 1
    elif x//2 == 0 :
        return D[x]
        c += 1
    else :
        x -= 1
        c += 1
    
    D[x] = DP[x]
    return c




    