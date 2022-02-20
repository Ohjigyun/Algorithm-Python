# 투 포인터를 활용해 다음과 같은 알고리즘으로 문제를 해결할 수 있다.
# 1. 시작점과 끝점이 첫 번째 원소의 인덱스를 가리키도록 한다.
# 2. 현재 부분 합이 M과 같다면 카운트한다.
# 3. 현재 부분 합이 M보다 작다면 end를 1 증가시킨다.
# 4. 현재 부분 합이 M보다 크거나 같다면 start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2번부터 4번까지를 반복한다.

n = 5
m = 5
data = [1,2,3,2,5]

count = 0
interval_sum = 0 
end = 0
#start를 차례대로 증가시키며 반복
for start in range(n):
#end를 가능한 만큼 이동 시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    #부분 합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
