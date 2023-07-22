count_of_rows = int(input("Введите количество рядов: "))
count_of_seats = int(input("Введите количество сидений в ряде: "))
count_distance_btwn_seats = int(input("Введите количество метров между сиденьями: "))

print("Сцена")
seat = "="
distance = "*"

scene_row = seat * count_of_seats
distance_btwn_seats = distance * count_distance_btwn_seats

for i in range(count_of_rows):
    print(scene_row, distance_btwn_seats, scene_row)
