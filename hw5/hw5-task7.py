import json

company_profit = 0
avg_profit = 0
profit = {}
aver_profit = {}
profit_list = []
i = 0
with open('test7.txt', 'r') as file:
    for line in file:
        name, firm, earnings, costs = line.split()
        profit[name] = int(earnings) - int(costs)
        if profit.setdefault(name) >= 0:
            company_profit += profit.setdefault(name)
            i += 1
    if i != 0:
        avg_profit = company_profit / i
    aver_profit = {'Средняя прибыль фирм': round(avg_profit)}
    profit_list = [profit, aver_profit]
    print(profit_list)

with open('test7.json', 'w', encoding='UTF-8') as file_json:
    json.dump(profit_list, file_json, ensure_ascii=False)
