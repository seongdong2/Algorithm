#셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.


def solution(s):
    answer = []
    s=s[2:-2]
    s=s.split('}.{')
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer :
                answer.append(int(j))
    
    return answer 