login_base = {}
counter = 0
while True:
    array_users = [item for item in input().split(" -> ")]
    if array_users[0] == "login":
        break
    else:
        login_base[array_users[0]] = array_users[1]

while True:
    array_logs = [item for item in input().split(" -> ")]
    if array_logs[0] == "end":
        break
    else:
        if array_logs[0] in login_base:
            if array_logs[1] == login_base[array_logs[0]]:
                print(f"{array_logs[0]}: logged in successfully")
            else:
                print(f"{array_logs[0]}: login failed")
                counter += 1
        else:
            print(f"{array_logs[0]}: login failed")
            counter += 1

print(f"unsuccessful login attempts: {counter}")