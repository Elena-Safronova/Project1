#  Игровое поле
board = [['-'] * 3 for _ in range(3)]  # генерация поля


def show_board(f):
    print("\n  0 1 2")  # верхняя разметка
    for i in range(len(f)):
        print(str(i)+' '+' '.join(f[i]))  # прорисовка поля


#  Ввод хода пользователя
def users_input(f):
    while True:
        place = input("\nВедите координаты (х у): ").split()
        # выбраковка по длине
        if len(place) != 2:
            print("Введите две координаты для х и у")
            continue
        # выбраковка не чисел
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числа")
            continue
        # инверсия координат для правельного отображения на поле
        y, x = map(int, place)
        # выбраковка значений вне диапозона
        if not ((0 <= x < 3) and (0 <= y < 3)):
            print("Вышли из диапазона")
            continue
        # проверка на свободу клетки
        if f[x][y] != '-':
            print("Клетка занята, выберете другую")
            continue
        break
    return x, y


# Проверка условий победы
def win_1v(f, value):
    # проверка на 3 одинаковых значения в строке
    def check_line(a1, a2, a3, token):
        if a1 == token and a2 == token and a3 == token:
            return True
        return False
    # проверка строки по полю: строка, столбец и диагонали
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], value) or \
                check_line(f[0][n], f[1][n], f[2][n], value) or \
                check_line(f[0][0], f[1][1], f[2][2], value) or \
                check_line(f[2][0], f[1][1], f[0][2], value):
            return True
    return False


# Игровой процесс
count = 0  # Подсчет кол-ва ходов
while count < 9:
    if count % 2 == 0:
        user = "X"
    else:
        user = "O"
    print(f"-----\nХод - {count+1}. Игрок - {user}.")
    show_board(board)
    x, y = users_input(board)
    board[x][y] = user
    if win_1v(board, user):
        print(f"-----\nИгра окончена - выиграл {user}.")
        show_board(board)
        break
    count += 1
else:
    print("-----\nИгра окончена - Ничья")
    show_board(board)
