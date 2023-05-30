num = int(input('수를 입력해주세요 '))
result = str
if num >= 1000000:
    num //= 1000000
    result = str(num)+'m'

print(result)