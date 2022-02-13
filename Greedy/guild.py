# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로
# '공포도'를 측정했는데 공포도가 높으면 대처 능력이 떨어집니다.
# 길드장은 길드를 안전하게 구성하고자 공포도가 X인 모험가는 반드시
# X명 이상으로 구성한 길드에 참여해야 여행을 떠날 수 있도록 했습니다. 
# 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)