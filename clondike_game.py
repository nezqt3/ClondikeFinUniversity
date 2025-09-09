from string import printable

def print_matrix(matrix):
    print(" ", *printable[10:20])
    for i in range(len(matrix)):
        print(i, *matrix[i])
        
def create_matrix():
    return [[0] * 10 for _ in range(10)]
        
matrix = create_matrix()

print_matrix(matrix)