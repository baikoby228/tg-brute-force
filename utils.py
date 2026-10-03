import time

def calc_time(start_time):
    print('time =', time.perf_counter() - start_time)