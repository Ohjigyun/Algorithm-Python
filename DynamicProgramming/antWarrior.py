# 개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량 창고를
# 몰래 공격하려고 합니다. 메뚜기 마을에는 여러 개의 식량 창고가
# 있는데 식량 창고는 일직선으로 이어져 있습니다.
# 각 식량 창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는
# 식량 창고를 선택적으로 약탈해 식량을 빼앗을 예정입니다.
# 이 때 메뚜기 정찰병들은 일직선상에 존재하는 식량 창고 중
# 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있습니다.
# 따라서 정찰병에게 들키지 않으려면 최소한 한 칸 이상 떨어진
# 창고를 약탈해야합니다. 개미 전사를 위해 식량 창고 N개에 대한
# 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는
# 프로그램을 작성하세요.

n = int(input())
array = list(map(int , input().split()))

#dp 테이블 초기화
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0] , array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])