year = int(input('년도를 입력해주세요. '))
leap = 0
if year % 4 == 0:
    leap = 1
    if year % 100 == 0:
        leap = 0
        if year % 400 == 0:
            leap = 1

if leap == True:
    print('윤년입니다.')
else:
    print('평년입니다')