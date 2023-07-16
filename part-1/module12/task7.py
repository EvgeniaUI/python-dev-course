def rock_paper_scissors():
    rock = "камень"
    scissors = "ножницы"
    paper = "бумага"
    hidden_object = rock
    user_object = input("Камень, ножницы или бумага?\n").lower()
    while user_object in (rock, scissors, paper):
        rock_scissors = hidden_object == rock and user_object == scissors
        scissors_paper = hidden_object == scissors and user_object == paper
        paper_rock = hidden_object == paper and user_object == rock
        if rock_scissors or scissors_paper or paper_rock:
            return "Вы проиграли!"
        elif hidden_object == user_object:
            print("Попробуйте еще раз.")
            user_object = input("Камень, ножницы или бумага?\n").lower()
        else:
            return "Вы выиграли!"
    return "Непонятная команда!"

def guess_the_number():
    hidden_number = 7
    user_unmber = int(input("Введите число: "))
    while user_unmber != hidden_number:
        user_unmber = int(input("Введите число: "))
    return "Вы угадали!"

def mainMenu():
    while 1:
        print("Меню:")
        print("1. игра 'Угадай число'")
        print("2. игра 'Камень, ножницы бумага'")
        motion = int(input("\nВведите номер игры: "))
        if motion == 1:
            print(guess_the_number() + "\n")
        elif motion == 2:
            print(rock_paper_scissors() + "\n")
mainMenu()