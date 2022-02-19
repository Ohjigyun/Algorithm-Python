# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다.
# 이 때 모든 알파벳을 오름차순으로 정렬해 출력하고 그 뒤에 모든 숫자를
# 더한 값을 이어서 출력하는 프로그램을 작성하세요.
# ex ) K1KA5CB7 이라는 값이 들어오면 ABCKK13을 출력합니다.

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))

