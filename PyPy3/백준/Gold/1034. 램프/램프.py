import sys

def max_lit_rows(N, M, lamp_rows, K):
    row_dict = {}  # 같은 행 패턴을 저장 딕셔너리
    max_count = 0  # 최대 행 개수

    for row in lamp_rows:
        row_str = "".join(row)  # 리스트 > 문자열 변환
        zero_count = row_str.count('0')  # 0 개수 카운팅
        
        # 0 개수 조건 확인 (K 이하 & 홀짝성 일치)
        if zero_count <= K and (K - zero_count) % 2 == 0:
            # 해당 패턴의 개수 증가
            if row_str in row_dict:
                row_dict[row_str] += 1
            else:
                row_dict[row_str] = 1
            
            # 최대값 갱신
            max_count = max(max_count, row_dict[row_str])

    return max_count

N, M = map(int, sys.stdin.readline().split())
lamp_rows = [list(sys.stdin.readline().strip()) for _ in range(N)]
K = int(sys.stdin.readline())

print(max_lit_rows(N, M, lamp_rows, K))
