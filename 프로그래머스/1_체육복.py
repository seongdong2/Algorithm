def solution(n, lost, reserve):
    def bollow(array, x):
        if array[x] != 0:
            array[x] = 0
            return True
        else : False
            
    #도난당한 친구들만큼 빼주기
    answer = n-len(lost)    
    chk = [0] * (n+1)
    
    #여벌 체육복 가져온 친구들 reserver
    for num in reserve:
        chk[num] += 1
    
    
    for i in range(1, n+1) :
        if i in lost :
            if bollow(chk, i-1) or bollow(chk, i+1):
                answer +=1 
   
    return answer