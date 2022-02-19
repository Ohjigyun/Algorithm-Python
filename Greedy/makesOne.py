# 어떠한 수 N이 1이 될 때까지 다음의 두 과정중 하나를 반복적으로
# 선택하여 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어
# 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을
# 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세요

n, k = map(int, input().split())
count = 0
while True:
    target = (n//k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += n - 1
print(count)