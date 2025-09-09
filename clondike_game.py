from string import printable

def print_matrix(matrix):
    print(" ", *printable[10:20])
    for i in range(len(matrix)):
        print(i + 1, *matrix[i])
        
def create_matrix():
    return [[0] * 10 for _ in range(10)]

def ask_for_move():
    move = input("Сделайте следующий ход: ")
    letter = "".join([ch for ch in move if ch.isalpha()])
    digit = int("".join([ch for ch in move if ch.isdigit()]))

    if (not letter or not digit) or (letter < "a" or letter > "j") or (digit < 1 or digit > 10): # нужно добавить проверку занята ли уже клетка которую выбирает игрок
        print("Вы ввели неправильные координаты. Попробуйте еще раз.")
        ask_for_move()
    else:
        return digit, letter
    
matrix = create_matrix()

print_matrix(matrix)