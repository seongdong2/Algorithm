n = int(input())
members = list(map(int, input().split()))
members.sort()

group = 0
max = 1
for member in range(n) :
    
    if max == members[member] :
        max = 1
        group += 1
    else :
        max += 1

print(group)    
    
