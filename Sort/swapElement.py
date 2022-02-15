# 동빈이는 두 개의 배열 A 와 B를 가지고 있습니다.
# 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
# 동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있으며
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 B에 있는 원소 하나를 골라서 바꾸는 것을 말합니다.
# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것입니다.
# N, K 그리고 배열 A,B의 정보가 주어졌을 때
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.

n , k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

#오름차순, 내림차순으로 정렬된 배열이기 때문에 첫 번째 인덱스부터
#확인하며 두 배열의 원소를 최대 k번을 비교한다.
for i in range(k):
    if a[i] < b[i]:
        a[i] , b[i] = b[i] , a[i]
    else:
        break

print(sum(a))