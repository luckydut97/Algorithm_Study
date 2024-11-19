def solution(targets):
    # 종료 지점 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    # 요격 미사일 개수
    missile_count = 0
    last_missile_position = -1  # 마지막 요격 미사일 위치
    
    for s, e in targets:
        # 현재 구간이 마지막 요격 미사일로 커버되지 않는 경우
        if s >= last_missile_position:
            missile_count += 1
            last_missile_position = e  # 새로운 미사일 발사
            
    return missile_count