def sum_up_diagonals(arr):
    total = 0

    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total