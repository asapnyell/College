def reverse(arr):
    revers = []
    for num in range(len(arr)):
        revers.append(arr[-(num + 1)]) # Adiciona os elementos da lista original de trás para frente
    return revers


def find_max(arr):
    max_array = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_array:
            max_array = arr[i]
    return max_array


def find_min(arr):
    min_array = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_array:
            min_array = arr[i]
    return min_array


def find_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


def palindromo(p1, p2):
    invert = ""
    for letter in p1:
        invert = letter + invert
    print(invert == p2)


def DNAtest(string):
    for letter in string:
        if letter not in "ACGT":
            return False
    return True


def DNAoRNA(string):
    rna = ""
    for letter in string:
        if letter == "T":
            rna += "U"
        else:
            rna += letter
    return rna


def maxArea(height):
    pass


def printMatrixHadamard(matrix):
    if not matrix: return
    # print matrix
    n = len(matrix)
    for i in range(n):
        linha = ''
        for j in range(n):
            if (matrix[i][j]):
                linha += "T "
            else:
                linha += "F "
        print(linha)


def Hadamard(n):
    pass


def show(matrix):
    s = "\n"
    # print array
    if not (isinstance(matrix[0], list)):
        linha = "\t"
        for e in matrix:
            linha += str(e) + '\t'
        s += linha + "\n"
    else:
        # print matrix
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            linha = '\t'
            for j in range(n):
                linha += str(matrix[i][j]) + '\t'
            s += linha + "\n"
    print(s)


def main():
    arr = [-3000, 100, 240, 120, -300, 1000]
    print('arr  ', arr)
    print('reverse ', reverse(arr))
    print('max ', find_max(arr), 'min ', find_min(arr))
    print('sum ', find_sum(arr), sum(arr))
    print('DNA  ', 'ACGTTA ', DNAtest('ACGTTA'))
    print('DNA : ', 'ACGT', ' RNA :', DNAoRNA('ACGT'))
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print('height :', height, 'max area :', maxArea(height))
    height = [1, 1]
    print('height :', height, 'max area :', maxArea(height))
    height = [1, 5, 6, 2, 5, 4, 8, 3]
    print('height :', height, 'max area :', maxArea(height))
    print('Hadamard(4)')
    printMatrixHadamard(Hadamard(4))
    show([[1], [2]])


main()

palindromo('ROMA', "POMAR")
