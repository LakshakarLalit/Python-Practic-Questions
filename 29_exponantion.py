import time 

wait_time = 1
max_retries = 5
attemts = 0

while attemts < max_retries:
    print("Attempts", attemts+1, "-Wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attemts+=1
