D = float(input("Ваш начальный Депозит "))
# Начальный депозит #Your deposit
K = float(input("Ежемесячные пополнение депозита[>=1]  "))
# Довложения каждый месяц # investments every month
g = 100
r = float(input("% дохода в Месяц на бирже или вкладе [5] "))
N = float(1 + r / g)  # float(input)("Процент доходности в месяц [1.05] ")
# Ождаемые проценты каждый месяц "5/100"
# interest rate per month % i
i = 1
# переменная для остановки счета
dep = float(D * N + K)
# Часть цикличиской формулы подсчета сложного %
c = float(input("Количество месяцев?[1-XX] "))
# количество месяцев# number of months
b = c + 1
# Переменная b для коректного отоброжения месяцев
while dep <= 333000111999:
    if i >= b:
       break

    print(dep, f"[{i}]_Месяц")
    dep = dep * N + K
    i = i + 1
print("Game over")
