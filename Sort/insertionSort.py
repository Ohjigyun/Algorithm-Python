array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1 , len(array)):
    for j in range(i, 0 , -1): # 인덱스 i부터 1까지 감소해 반복하는 문법
        if array[j] < array[j-1]: #왼쪽으로 한 칸씩 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 멈춤
            break
print(array)
#[0,1,2,3,4,5,6,7,8,9]