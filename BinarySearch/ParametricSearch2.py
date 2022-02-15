# 정렬된 배열에서 특정 수의 개수 구하기

# N 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이 때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# (시간복잡도는 O(logN)이 아니면 시간 초과 판정을 받습니다.)

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n , x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x , x )

if count == 0:
    print(-1)
else:
    print(count)
