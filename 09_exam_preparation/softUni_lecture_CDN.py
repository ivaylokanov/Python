import datetime
from datetime import timedelta

lectures = []
max_duration = 10 * 60 * 60
current_duration = 0
server_counter = 1
elements_choice_duration = 0
time_format = "%H:%M:%S"
while True:
    line = input()
    line = line.replace(":", "=")
    if line[0:6] == "scrape":
        tokens = line.split(" ")
        key_token = tokens[1]
        value_token = tokens[2]
        break
    elements = line.split(";")
    for element in elements:
        if element[0:7] == "trainer":
            trainer = element
        elif element[0:7] == "lecture":
            lecture = element
        elif element[0:6] == "course":
            course = element
        elif element[0:8] == "duration":
            str_duration = element
            str_duration = str_duration.replace("m", "")
            str_duration = str_duration.replace("duration=","")
            sec = str_duration.split("h")
            hours_sec = int(sec[0])*60*60
            second = int(sec[1])*60
            duration = hours_sec + second
        else:
            print("problem")
    if max_duration < current_duration + duration:
        current_duration = duration
        server_counter = server_counter + 1
    else:
        current_duration = current_duration +duration

    lectures.append(f"https://streamcdn{server_counter}.softuni.bg/{course}&{lecture}&{trainer}:::{duration}")

for lecture in lectures:
    if lecture.find(f"{key_token}={value_token}") != -1:
        elements_choice = lecture.split(":::")
        print(elements_choice[0])

        elements_choice_duration += int(elements_choice[1])

hours = elements_choice_duration//3600
minutes = int((elements_choice_duration - hours*3600)/60)
print(f"total duration: {hours:02}:{minutes:02}:00")