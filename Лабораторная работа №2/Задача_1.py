money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0
while True:
    diff = spend - salary
    if diff > money_capital:
        break
    money_capital -= diff
    spend *= 1 + increase
    count += 1


print("Количество месяцев, которое можно протянуть без долгов:", count)
