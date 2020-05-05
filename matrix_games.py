import numpy as np
import colorama


def pretty_print(matrix):
    row_mins = np.argmin(matrix,axis=1)
    col_maxs = np.argmax(matrix,axis=0)
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if col == row_mins[row] and row == col_maxs[col]:
                color = colorama.Fore.GREEN
            elif col == row_mins[row]:
                color = colorama.Fore.BLUE
            elif row == col_maxs[col]:
                color = colorama.Fore.RED
            else:
                color = colorama.Fore.RESET

            print(f'{color}{matrix[row,col]:3}', end=' ')
        print(colorama.Fore.RESET)

while True:
    print('Matrix size:')
    size = int(input())
    matrix = np.random.randint(-10, 10, size=(size,size))
    pretty_print(matrix)


    first = np.random.randint(0,1)

    if first:
        print('Row First Move? ')
        pick = int(input()) - 1
        vec = matrix[pick]
        min_ = np.min(vec)
        print(f"I pick {min_}!")
        best = np.max(np.min(matrix, axis=1))
        print(f"Your best was {best}")
    else:
        print('Col First Move? ')
        pick = int(input()) - 1
        vec = matrix[:,pick].flatten()
        max_ = np.max(vec)
        print(f"I pick {max_}!")
        best = np.min(np.max(matrix, axis=0))
        print(f"Your best was {best}")
