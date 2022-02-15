# 동빈이는 여행가신 부모님을 대신해 떡볶이 떡을 만들기로 했습니다
# 떡볶이 떡은 한봉지 안에 들어가는 총 길이는 절단기로 잘라 동일하나
# 절단된 떡의 길이는 일정하지 않습니다.
# 예를 들어 19, 14, 10, 17 인 떡을 15로 지정된 절단기로 자르면 떡의 길이는
# 15, 14, 10, 15가 되며 절단된 떡의 길이는 4, 0 , 0 , 2입니다.
# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요


n , m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+ end) //2
    for x in array:
        #잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x- mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽)            
    if total < m:
        end = mid - 1
    # 떡의 양이 충분하면 덜 자르기 (오른쪽)
    else:
        result = mid
        start = mid + 1
print(result)