def solution(left, right):
    answer = 0
    
    def count(x):
        cnt=0
        
        if x == 1:
            return 1
        
        
        for i in range(1, ((x+1)//2)+1):
            if x%i == 0:
                cnt += 1
        
        if cnt % 2 != 0:
            cnt -= 1
            cnt *= 2
            cnt += 1
        else :
            cnt *=2
        
        return cnt+2
            
        
    for num in range(left, right+1):
        if count(num) % 2 == 0:
            answer -= num
        else: 
            answer += num
    
    return answer