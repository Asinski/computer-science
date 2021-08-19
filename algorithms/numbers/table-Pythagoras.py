from prettytable import PrettyTable, ALL

multiplication_table = PrettyTable(header=False, hrules=ALL)
for i in range(1, 21):
    multiplication_table.add_row([i * j for j in range(1, 21)])
multiplication_table.align = "r"
print(multiplication_table)
