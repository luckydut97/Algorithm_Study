def solve():
    N = 9
    num = sum(lst)-100              # 찾아야 할 숫자를 계산
    for i in range(N-1):
        for j in range(i+1, N):     # N개중에서 2개를 뽑는 모든 조합
            if lst[i]+lst[j]==num:
                return lst[i], lst[j]

lst = [int(input()) for _ in range(9)]
n, m =solve()   # 7명에 포함되지 않는 2명 찾기
for i in sorted(lst):
    if i!=n and i!=m:
        print(i)