positionX, positionY = 8, 10

north = ["W", "w"]
south = ["S", "s"]
west = ["A", "a"]
east = ["D", "d"]
while 1:
    command_move = input(f"Марсоход находится на позиции {positionX}, {positionY}, введите команду:")
    if command_move in north and positionY < 20:
        positionY += 1
    if command_move in south and positionY > 0:
        positionY -= 1
    if command_move in west and positionX > 0:
        positionX -= 1
    if command_move in east and positionX < 15:
        positionX += 1
