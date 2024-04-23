import time
current_time = time.time()
timestamps = [current_time + i*3600 for i in range(1, 6)]  # Generate timestamps for the next 5 hours
print("Scheduled Events:")
for timestamp in timestamps:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)))
