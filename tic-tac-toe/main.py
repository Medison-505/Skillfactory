# Я на 120% уверена, что этот код не будут читать люди, которые не говорят на русском языке.

# Players greeting
def greeting():
    print('Это игра крестики-нолики.')
    print('Чтобы сделать ход укажите координаты ячейки: номер строки пробел номер столбца.')
    print('Например, если вы хотите пойти в левый верхний угол введите "0 0".')
    print()


# Create a game board
field = [[" "] * 3 for i in range(3)]


# print a game board
def show_game_board():
    print(f'  0 1 2')
    for i in range(3):
        row = ' '.join(field[i])
        print(f'{i} {row}')


# Ask coordinates
def ask_coordinates():
    while True:
        coordinates = input('Введите координаты: ').split()

        if len(coordinates) != 2:
            print('Ведите две координаты.')
            continue

        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числовые координаты.')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона.')
            continue

        if field[x][y] != " ":
            print('Клетка уже занята.')
            continue

        return x, y


# Check winner
def check_win():
    win_coordinates = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))
    )

    for coordinates in win_coordinates:
        symbols = []
        for c in coordinates:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    return False


# Moving loop
greeting()

move_count = 0

while True:
    move_count += 1

    show_game_board()

    if move_count % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = ask_coordinates()

    if move_count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if move_count == 9:
        print('Ходов больше нет. Ничья.')
        break

print('Игра окончена.')
