import time

def focus_clock(minutes):
    seconds = minutes * 60

    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes_remaining = int(remaining_time // 60)
        seconds_remaining = int(remaining_time % 60)

        timer_display = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        print(timer_display, end="\r")
        time.sleep(1)

    print("Time's up!")

# 设置专注时长为2500分钟
focus_time = 2500000
focus_clock(focus_time)
