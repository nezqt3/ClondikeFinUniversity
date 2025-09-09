def print_matrix(matrix):
    for i in range(len(matrix)):
        print(i + 1, *matrix[i])
        
print_matrix([[0, 0], [0, 0], [0, 0]])