file = float(input("Укажите размер файла для скачивания: "))
speed = float(input("Какова скорость вашего соединения: "))

downloaded = speed
secs = 1
while downloaded < file:
    persent = round(downloaded / file * 100)
    print(f"Прошло {secs} сек. Скачано {downloaded} из {file} Мб ({persent}%)")
    downloaded += speed
    secs += 1
print(f"Прошло {secs} сек. Скачано {file} из {file} Мб (100%)")
