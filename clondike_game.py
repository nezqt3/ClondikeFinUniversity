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
    

def ask_for_move():
    move = input("Сделайте следующий ход: ")
    try:
        letter = "".join([ch for ch in move if ch.isalpha()])
        digit = int("".join([ch for ch in move if ch.isdigit()]))
        len(letter) == 1
        len(digit) == 1
    except:
        print("Вы ввели неправильные координаты. Попробуйте еще раз.")
        return ask_for_move()

    if (not letter or not digit) or (letter < "a" or letter > "j") or (digit < 1 or digit > 10) or (matrix[digit - 1][return_number_columns(letter)] == 1): # нужно добавить проверку занята ли уже клетка которую выбирает игрок
        print("Вы ввели неправильные координаты. Попробуйте еще раз.")
        return ask_for_move()
    else:
        return digit, letter
    
matrix = create_matrix()
print_matrix(matrix)

print(print_rules())

while True:
    digit, letter = ask_for_move()
    matrix[digit - 1][return_number_columns(letter)] = 1
    
    print_matrix(matrix)
