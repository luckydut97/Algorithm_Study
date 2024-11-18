def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열을 초로 변환하는 함수
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds

    # 초를 시간 문자열로 변환하는 함수
    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02}:{seconds:02}"

    # 입력된 시간을 초 단위로 변환
    video_len_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)

    # 시작 위치가 오프닝 구간에 있으면 이동
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    # 명령어 처리
    for command in commands:
        if command == "prev":
            pos_sec = max(0, pos_sec - 10)
        elif command == "next":
            pos_sec = min(video_len_sec, pos_sec + 10)

        # 명령 실행 후 오프닝 구간에 있으면 이동
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    # 최종 위치를 문자열로 변환하여 반환
    return seconds_to_time(pos_sec)
