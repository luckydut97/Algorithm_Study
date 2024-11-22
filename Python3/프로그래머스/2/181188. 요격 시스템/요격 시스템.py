def solution(targets):
    
    # 종료 지점 기준으로 정렬
    targets=sorted(targets)

    
    answer=1 #요격횟수
    aim_start, aim_end = targets.pop(0) #현재 조준범위
    
    
    for target in targets:
        #꺼내오기
        target_start, target_end = target
        
        # 다음 범위의 최소 < 조준 범위의 최대: 요격횟수그대로
        if target_start < aim_end:
            #조준범위를 좁힌다.
            aim_start= max(aim_start, target_start) #조준범위의 x좌표 갱신
            aim_end= min(aim_end,target_end) #조준범위의 y좌표 갱신
            
        else:
            aim_start,aim_end=target_start, target_end
            #요격횟수추가
            answer+=1
            
        
    
        
    return answer