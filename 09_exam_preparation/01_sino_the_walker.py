import datetime
current_time = datetime.time()
time_in_sec = int(current_time[0])*3600 + int(current_time[1])*60 + int(current_time[2])
steps = int(input())
time_for_each_step = int(input())
total_time = time_in_sec + steps*time_for_each_step

a = str(datetime.timedelta(seconds=total_time))
az = a[len(a)-7:len(a)]
print(f"Time Arrival: {az}")