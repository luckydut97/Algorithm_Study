n = int(input())  # 사용자로부터 전체 선수 수를 입력받음
graph = [list(map(int, input().split())) for _ in range(n)]  # 각 선수 간의 능력치를 2차원 배열로 입력받음
members = list(range(n))  # 모든 선수의 번호를 리스트로 생성
min_value = float('inf')  # 최소 능력치 차이를 저장할 변수, 무한대로 초기화

# 주어진 팀의 점수를 계산하는 함수
def calculate_score(team):
    score = 0  # 팀의 점수
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            # 팀 내 선수들 간의 상호작용 점수를 합산
            score += graph[team[i]][team[j]] + graph[team[j]][team[i]]
    return score  # 계산된 팀 점수 반환

# 조합을 생성하는 재귀 함수
def combinations(arr, n, new_arr, c):
    if len(new_arr) == n:  # 기준 길이에 도달하면
        start_team = new_arr  # 현재 조합을 start_team으로 설정
        link_team = list(set(members) - set(start_team))  # 나머지 선수들로 link_team 구성
        global min_value  # 전역 변수 min_value 사용
        # 두 팀의 점수 차이를 계산하여 최소값 업데이트
        min_value = min(min_value, abs(calculate_score(start_team) - calculate_score(link_team)))
        return

    for i in range(c, len(arr)):
        # 재귀 호출하여 조합 계속 생성
        combinations(arr, n, new_arr + [arr[i]], i + 1)

combinations(members, n // 2, [], 0)  # 조합 생성 함수 호출
print(min_value)  # 계산된 최소 능력치 차이 출력