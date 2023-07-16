boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девочек: "))

if boys > girls:
    max_cnt, min_cnt = boys, girls
    max_letter, min_letter = 'B', 'G'
else:
    max_cnt, min_cnt = girls, boys
    max_letter, min_letter = 'G', 'B'
if max_cnt / min_cnt > 2:
    print("Нет решения")
else:
    count_min_left, count_max_left = min_cnt, max_cnt - 1
    result_string = max_letter
    for i in range(max_cnt + min_cnt - 2):
        if result_string[-1] == min_letter:
            result_string += max_letter
            count_max_left -= 1
            if 0 < count_min_left < count_max_left:
                result_string += max_letter
                count_max_left -= 1
        else:
            result_string += min_letter
            count_min_left -= 1
    print(result_string)
