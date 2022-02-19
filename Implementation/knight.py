# 왕실 정원은 8 X 8 의 좌표 평면입니다.
# 왕실 전원의 특정한 한 칸에 나이트가 서있습니다.
# 나이트는 말을 타고있어 L자 형태로만 이동할 수 있으며
# 정원 밖으로는 나갈 수 없습니다.
# 나이트는 2가지 경우로 이동할 수 있습니다
# 1. 수평으로 두 칸 이동한 뒤 수직으로 한 칸 이동
# 2. 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동

data = input()
row = int(data[1])
col = int(ord(data[0]))- int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1) , (1, 2) , (-1 , 2) , (-2 , 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <=8 and next_col >=1 and next_col <= 8:
        result += 1

print(result)

