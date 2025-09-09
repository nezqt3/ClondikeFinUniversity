from string import printable

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
        digit, letter = int(move.split()[0]), move.split()[1]
    except:
        print("Вы ввели неправильные координаты. Попробуйте еще раз.")
        return ask_for_move()

    if (not letter or not digit) or (letter < "a" or letter > "j") or (digit < 1 or digit > 10): # нужно добавить проверку занята ли уже клетка которую выбирает игрок
        print("Вы ввели неправильные координаты. Попробуйте еще раз.")
        return ask_for_move()
    else:
        return digit, letter
    
matrix = create_matrix()

digit, letter = ask_for_move()
print(return_number_columns(letter))
