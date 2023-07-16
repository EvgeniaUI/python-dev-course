def pendulum(begin, end):
    temp = begin
    counter = 0
    while temp > end:
        temp *= (1 - 84/1000)
        counter += 1
    return counter

begin = float(input("Введите начальную амплитуду: "))
end = float(input("Введите амплитуду остановки: "))

print(f"Маятник считается остановившимся через {pendulum(begin, end)} колебаний")
