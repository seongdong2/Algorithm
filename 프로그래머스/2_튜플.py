#셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.


def solution(s):
    answer = num(s)
    #answer = []
    return answer

def num(x):
    _num = []
    list_num = []
    
    for i in range(len(x)):
        if x[i] == '{' or x[i] =='}':
            continue
        
        if x[i] == ',' and x[i-1] == '}' and x[i+1]=='{' :
                list_num.append(_num)
                _num = []
        
        if x[i] != ',':
            _num.append(int(x[i]))
            
    list_num.append(_num)
    return list_num