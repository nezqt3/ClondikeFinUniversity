from string import printable


def print_rules():
    return """
Игра ведётся на игровом поле размером 10 на 10 клеток. 
Игроки по очереди выставляют в любую свободную клетку по отметке, и тот игрок, 
после чьего хода получилась цепочка длиной хотя бы в три отметки, проигрывает. 
При этом в цепочке считаются как свои отметки, так и отметки соперника, у игровых 
фишек как бы нет хозяина. Цепочка — это ряд фишек, следующая фишка в котором примыкает к 
предыдущей с любого из восьми направлений.
    """

def print_matrix(matrix):
    print("  ", *printable[10:20])
    for i in range(len(matrix)):
        if i == 9:
            print(i + 1, *matrix[i])
        else:
            print(i + 1, "", *matrix[i])
        
def create_matrix():
    return [[0] * 10 for _ in range(10)]

def return_number_columns(letter):
    dict = {printable[10:20][i]: i for i in range(10)}
    return dict[letter]
    
def check_winner(matrix, row, column):
    return False

def ask_for_move():
    move = input("Сделайте следующий ход: ")
    try:
        digit, letter = int(move.split()[0]), move.split()[1]
    except:
        print("Вы ввели неправильные координаты. Попробуйте еще раз.")
        return ask_for_move()

    if (not letter or not digit) or (letter < "a" or letter > "j") or (digit < 1 or digit > 10) or (matrix[digit - 1][return_number_columns(letter)] == 1):
        if matrix[digit - 1][return_number_columns(letter)] == 1:
            print("Данная ячейка уже занята. Попробуйте еще раз")
            return ask_for_move()
        else:
            print("Вы ввели неправильные координаты. Попробуйте еще раз.")
            return ask_for_move()
    else:
        return digit, letter
    
matrix = create_matrix()
print_matrix(matrix)

print(print_rules())

while True:
    row_number, letter = ask_for_move()
    column_number = return_number_columns(letter)
    
    matrix[row_number - 1][column_number] = 1
    
    if check_winner(matrix, row_number, column_number):
        print("Вы победили")
        break
    
    print_matrix(matrix)
    
    