shell_by_region = {}
while True:
    splited_line = input().split()
    region = splited_line[0]
    if region == "Aggregate":
        break
    shell = int(splited_line[1])
    if region not in shell_by_region:
        shell_by_region[region] = []
        shell_by_region[region].append(shell)
    elif shell not in shell_by_region[region]:
        shell_by_region[region].append(shell)
    else:
        continue
for key, value in shell_by_region.items():
    giant_shell = sum(value) - sum(value)//len(value)
    print(f"{key} -> ", end="")
    print(*value, sep=", ", end="")
    print(f" ({giant_shell})")
