import math
budget = float(input())
servers = int(input())
storage = int(input())
hosts = int(input())
up_time = float(input())
servers_need = math.ceil(servers/50)
storage_need = storage/0.5
total_costs = (servers_need*2 + storage_need*0.5)*24*30 + hosts*10
total_costs = total_costs*up_time/100
calculation = budget - total_costs
if calculation>=0:
    print(f"Clouds Ahoy! Monthly cost: ${total_costs:.2f} (${calculation:.2f} leftover)")
else:
    calculation = calculation*(-1)
    print(f"Stay Grounded! Monthly cost: ${total_costs:.2f} (Need ${calculation:.2f} more)")
