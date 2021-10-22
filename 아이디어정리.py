import 정리

#기본문법
##enumerate
a= ['hong', 'gil', 'dong']
b= []
c= {}
for i, name in enumerate(a):
    b.append((i, name))
    c[i] = b[name]

##lambda x, y:x, y
print(lambda x, y, z : x+y-z)(3, 4, 9)
lambdas=[lambda x:x+10, lambda x:x+100]
print(lambdas[0](5))

#구현
정리.DP
정리.DP2
#아이디어
#객체를 최대한 잘 활용한다
#최대한 곱해줘야 크다
#모든 상황을 셈하기가 가능할 때, 모든 경우의 수를 계산하도록 한다.

#정렬
정리.quick
정리.count

#해시
정리.hash

#완전탐색
정리.bi
정리.dfs
정리.bfs

#기본 아이디어
#1. 함수는 방문하지 않은 장소를 완전하게 탐색할 방법으로 만들어진다.
#2. 상황에 맞게 함수를 적용시킨다

#활용 아이디어
#1. 모든 거리가 1일 때 너비 탐색을 시작한다.
#2. 모든 상황을 셈하기가 가능할 때, 모든 경우의 수를 계산하도록 한다.




