# Я на 120% уверена, что этот код не будут читать люди, которые не говорят на русском языке.

# Создаем игровое поле
print('Это игра крестики-нолики. \nЧтобы сделать ход укажите координаты ячейки: номер строки затем номер столбца. '
      '\nНапример, если вы хотите пойти в левый верхний угол введите 00')
print()

game_board = [[' ', '0', '1', '2'],
              ['0', '-', '-', '-'],
              ['1', '-', '-', '-'],
              ['2', '-', '-', '-']]

for row in game_board:
    for col in row:
        print(col, end=' ')
    print()


# Приглашаем игрока ко вводу и устанавливаем координаты хода

def player_move_func(player_move, team):
    print()
    player_move = list(map(int, input('Вы играете за игрока ' + team + '. Введите координаты своего хода.')))
    print()
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            game_board[player_move[0] + 1][player_move[1] + 1] = team
            print(game_board[i][j], end=' ')
        print()


# Цикл ходов
move_count = 0

player_move_func('x_player_move', 'X')

while move_count < 8:
    player_move_func('o_player_move', '0')

    if (game_board[1][1] == '0' and game_board[2][2] == '0' and game_board[3][3] == '0' or
            game_board[1][3] == '0' and game_board[2][2] == '0' and game_board[3][1] == '0' or
            game_board[1][1] == '0' and game_board[1][2] == '0' and game_board[1][3] == '0' or
            game_board[2][1] == '0' and game_board[2][2] == '0' and game_board[2][3] == '0' or
            game_board[3][1] == '0' and game_board[3][2] == '0' and game_board[3][3] == '0' or
            game_board[1][1] == '0' and game_board[2][1] == '0' and game_board[3][1] == '0' or
            game_board[1][2] == '0' and game_board[2][2] == '0' and game_board[3][2] == '0' or
            game_board[1][3] == '0' and game_board[2][3] == '0' and game_board[3][3] == '0'):
        print('Игрок 0 победил!')
        break

    player_move_func('x_player_move', 'X')

    if (game_board[1][1] == 'X' and game_board[2][2] == 'X' and game_board[3][3] == 'X' or
            game_board[1][3] == 'X' and game_board[2][2] == 'X' and game_board[3][1] == 'X' or
            game_board[1][1] == 'X' and game_board[1][2] == 'X' and game_board[1][3] == 'X' or
            game_board[2][1] == 'X' and game_board[2][2] == 'X' and game_board[2][3] == 'X' or
            game_board[3][1] == 'X' and game_board[3][2] == 'X' and game_board[3][3] == 'X' or
            game_board[1][1] == 'X' and game_board[2][1] == 'X' and game_board[3][1] == 'X' or
            game_board[1][2] == 'X' and game_board[2][2] == 'X' and game_board[3][2] == 'X' or
            game_board[1][3] == 'X' and game_board[2][3] == 'X' and game_board[3][3] == 'X'):
        print('Игрок Х победил!')
        break

    move_count += 2
else:
    print()
    print('Ходов больше нет.')

print('Игра окончена.')



