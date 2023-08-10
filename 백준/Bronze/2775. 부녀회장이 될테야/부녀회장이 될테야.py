import sys

t = int(sys.stdin.readline())

# 아파트 초기화
apartment = [[0 for _ in range(15)] for _ in range(15)]

# 0층 값 지정
for i in range(15):
    apartment[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        apartment[i][j] = apartment[i-1][j] + apartment[i][j-1]

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(apartment[k][n])