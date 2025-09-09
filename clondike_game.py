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

def ask_for_move():
    move = input("Сделайте следующий ход: ")
    letter = "".join([ch for ch in move if ch.isalpha()])
    digit = int("".join([ch for ch in move if ch.isdigit()]))

    if (not letter or not digit) or (letter < "a" or letter > "j") or (digit < 1 or digit > 10): # нужно добавить проверку занята ли уже клетка которую выбирает игрок
        return None
    else:
        return digit, letter
    
matrix = create_matrix()

print_matrix(matrix)

while True:
    pass