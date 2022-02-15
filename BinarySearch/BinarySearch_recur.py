#이진 탐색(재귀)
def binary_search(array , target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 mid 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작으면 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #아니면 오른쪽 확인
    else:
        return binary_search(array, target, mid+1 , end)

n , target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0 , n-1)
if result == None:
    print("-1")
else:
    print( result + 1 )