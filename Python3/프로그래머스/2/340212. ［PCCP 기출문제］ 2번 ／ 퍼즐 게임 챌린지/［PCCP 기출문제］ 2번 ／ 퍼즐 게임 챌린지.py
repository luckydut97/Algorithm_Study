def solution(diffs, times, limit):
    def can_solve(level):
        total_time = 0
        time_prev = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            
            if diff <= level:
                # 숙련도가 충분한 경우
                total_time += time_cur
            else:
                # 숙련도가 부족한 경우
                fail_count = diff - level
                total_time += (time_cur + time_prev) * fail_count + time_cur
            
            # 시간 초과하면 False 반환
            if total_time > limit:
                return False
            
            # 현재 퍼즐의 시간을 이전 퍼즐의 시간으로 저장
            time_prev = time_cur
        
        return True

    # 이분 탐색 설정
    left = 1  # 최소 숙련도
    right = max(diffs)  # 최대 숙련도
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_solve(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer