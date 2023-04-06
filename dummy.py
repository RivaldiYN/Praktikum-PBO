def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])

    # create a new array with the rows and cols swapped
    transposed_arr = [[arr[j][i] for j in range(rows)] for i in range(cols)]
    
    return transposed_arr
x, y = map(int, input("Masukkan lebar dan panjang array: ").split())

# Inputan array pertama
array = []
for i in range(x):
    row = transpose(map(int, input().split()))
    if len(row) != y:
        print("-1")
        exit()
    array.append(row)

# Mengecek apakah dimensi array sesuai dengan input pertama
if len(array) != x:
    print("-1")
    exit()
for i in range(x):
    if len(array[i]) != y:
        print("-1")
        exit()

# Melakukan transpose pada array
array_transpose = [[array[j][i] for j in range(x)] for i in range(y)]

# Mencetak hasil transpose
for row in array_transpose:
    print(*row)