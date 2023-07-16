import math

R = float(input("Введите радиус случайной планеты: "))

v_earth = 1.08321 * 10 ** 12

v_other = 4 / 3 * math.pi * R ** 3

earth_times = v_earth / v_other

if earth_times > 1:
    print(f"Объём планеты Земля больше в {round(earth_times, 3)} раз")
else:
    print(f"Объём планеты Земля меньше в {round(1 / earth_times, 3)} раз")
