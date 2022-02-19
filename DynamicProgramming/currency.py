# N 가지 종류의 화폐가 있습니다.
# 이 화폐들의 개수를 최소한으로 이용해 그 가치의 합이 M원이 되도록
# 하려고 합니다. 이 때 각 종류의 화페는 몇 개라도 사용할 수 있습니다.
# M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

n , m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i] , m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j] , d[j - array[i]] +1 )
if d[m] == 10001:
    print(-1)
else:
    print(d[m])