import 1
import 2
def main():
    print("Игры")
    print('1.Угадай число')
    print('2.Блэк_Джэк')
    print('0.Выход')

    Выбор = input("Выбери игру: ")
    if Выбор == "1":
        1.play_game()
    elif Выбор == "2":
        2.play_game()
    elif Выбор == "0":
        print("Выход")
    else:
        print('Неверный ввод')
if __name__ == "__main__":
    main()
