#입력
x, y = map(int, input().split())

#월별 일수 및 요일 선언
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

# 총 일 수 계산
total_days = y
for i in range(x):
    total_days += month[i]

# 총 일 수를 7로 나눈 나머지를 구함
tmp = total_days % 7

# 요일 출력
print(week[tmp])