# Division and Conquest Template
def binarySearch(alist,key):
    def body(alist,key,low,high):
        mid=(low+high) //2
        if low > high: # base case
            return -1    
        elif key == alist[mid]:  # base case
            return mid
        elif key < alist[mid]: # division
                  # Gets the position of the element in the left half 
            return body(alist,key,low,mid-1)
        else: # division
                  # Gets the position of the element in the right half 
                return body(alist,key,mid+1,high)
    return body(alist,key,0,len(alist)-1)

def isPalindrome(word):
       # base case #1
    if (len(word) <= 1):
        return True
       # base case #2  and combination
    if (word[0] != word[-1]):
        return False
       # division
    return isPalindrome(word[1:-1])
     
# Function to find the maximum number
# in a given array.
def find_max(arr):
    def body(arr,lo,hi):
        if lo == hi: # Caso base: se há apenas um elemento, ele é o máximo
            return arr[lo]
        mid = (lo + hi) // 2
              # Get the maximum element from the left half
        left_max = body(arr, lo, mid) # Chamada recursiva na metade esquerda
        right_max = body(arr, mid + 1, hi) # Chamada recursiva na metade direita
        return left_max if left_max >  right_max else right_max # Combinação dos resultados
    return body(arr,0,len(arr)-1)


def find_min(arr):
    def body(arr, lo, hi):
        if lo == hi:  # Caso base: se há apenas um elemento, ele é o máximo
            return arr[lo]
        mid = (lo + hi) // 2
        left_min = body(arr, lo, mid)
        right_min = body(arr, mid + 1, hi)
        return min(left_min, right_min)
    return body(arr, 0, len(arr) - 1)

def find_sum(arr):
    def body(arr, lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        left_sum = body(arr, lo, mid)
        right_sum = body(arr, mid + 1, hi)
        return left_sum + right_sum
    return body(arr, 0, len(arr) - 1)

def searchPosition(arr,target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

#from bisect import bisect_left, bisect_right
def bisect_right(arr,target):
    return bisect.bisect_right(arr, target)

def bisect_left(arr,target):
    return bisect.bisect_left(arr, target)

def countFreq(arr, target):    
    low = bisect_left(arr, target)
    righ = bisect_right(arr, target)
    #print(low,righ)    
    # Return the difference between upper bound and 
    # lower bound of the target
    return righ - low

def recursiveSearch2DMatrix(mat, x):
    def search(mat, row_low, row_high, col_low, col_high):
        if row_low > row_high or col_low > col_high:
            return False
        row_mid = (row_low + row_high) // 2
        col_mid = (col_low + col_high) // 2
        if mat[row_mid][col_mid] == x:
            return True
        elif mat[row_mid][col_mid] < x:
            return search(mat, row_mid + 1, row_high, col_low, col_high) or search(mat, row_low, row_high, col_mid + 1, col_high)
        else:
            return search(mat, row_low, row_mid - 1, col_low, col_high) or search(mat, row_low, row_high, col_low, col_mid - 1)
    return search(mat, 0, len(mat) - 1, 0, len(mat[0]) - 1)


def prob1():
    print('Binary Search\nExemplo 1 :')
    arr = [1,3,5,6]; target = 5
    print('Entrada:',arr,target)
    print('Saída : True')
    res = binarySearch(arr, target)
    print(True if res>=0 else False)
    arr = [1, 3, 3, 4, 4, 4, 4, 7, 8, 8];  target = 4
    print('Entrada:',arr,target)
    print('Saída  : True')
    res = binarySearch(arr, target)
    print(True if res>=0 else False)
    arr = [1, 3, 3, 4, 4, 4, 4, 7, 8, 8];  target = 40
    print('Entrada:',arr,target)
    print('Saída  : False')
    res = binarySearch(arr, target)
    
def prob2():
    print('isPalindrome\nExemplo 1 :')
    word = 'arara'
    print('Entrada:',word)
    print('Saída : True')
    print(isPalindrome(word))
    print('isPalindrome\nExemplo 2 :')
    word = 'aa'
    print('Entrada:',word)
    print('Saída : True')
    print(isPalindrome(word))
    word = 'aai'
    print('Entrada:',word)
    print('Saída : False')
    print(isPalindrome(word))

def prob3():
    print('maximum\nExemplo 3 :')
    arr = [1, 2, 2, 2, 2,2,2, 7, 8, 8]
    print('Entrada:',arr)
    print('Saída : 8')
    print(find_max(arr))
    print('Exemplo 2 :')
    arr = [100, -20, 2, 33, 430,-2,2, 40, 8, 90]
    print('Entrada:',arr)
    print('Saída : 430')
    print(find_max(arr))

def prob4():
    print('minimum\nExemplo 4 :')
    arr = [1, 2, 2, 2, 2,2,2, 7, 8, 8]
    print('Entrada:',arr)
    print('Saída : 1')
    print(find_min(arr))
    print('Exemplo 2 :')
    arr = [100, -20, 2, 33, 430,-2,2, 40, 8, 90]
    print('Entrada:',arr)
    print('Saída : -20')
    print(find_min(arr))

def prob5():
    print('sum\nExemplo 5 :')
    arr = [1, 2, 2, 2, 2,2,2, 7, 8, 8]
    print('Entrada:',arr)
    print('Saída : ',sum(arr))
    print(find_sum(arr))
    print('Exemplo 2 :')
    arr = [100, -20, 2, 33, 430,-2,2, 40, 8, 90]
    print('Entrada:',arr)
    print('Saída : ',sum(arr))
    print(find_sum(arr))

def prob6():
     print('searchPosition\nExemplo 8 :')
     nums = [1,3,5,6];target = 5
     print('nums : ',nums, 'target : ',target)
     print(searchPosition(nums,target))
     nums = [1,3,5,6]; target = 2
     print('nums : ',nums, 'target : ',target)
     print(searchPosition(nums,target))
     nums = [1,3,5,6]; target = 7
     print('nums : ',nums, 'target : ',target)
     print(searchPosition(nums,target))

#from bisect import bisect_left, bisect_right 
def prob7():
    print('Bisect right / left\nExemplo 1 :')
    arr = [1,3,5,6]; target = 5
    print('Entrada:',arr,target)
    print('Saída bisect left : 2, Saída bisect right: 3 ')
    print(bisect_left(arr, target),bisect_right(arr, target))
    arr = [1, 3, 3, 4, 4, 4, 4, 7, 8, 8];  target = 4
    print('Entrada:',arr,target)
    print('Saída bisect left : 3, Saída bisect right: 7 ')
    print(bisect_left(arr, target),bisect_right(arr, target))
    arr = [1, 3, 3, 4, 4, 4, 4, 7, 8, 8];  target = 40
    print('Entrada:',arr,target)
    print('Saída bisect left : 10, Saída bisect right: 10 ')
    print(bisect_left(arr, target),bisect_right(arr, target))

def prob8():
    print('countFreq \nExemplo 1 :')
    arr = [1, 2, 2, 2, 2,2,2, 7, 8, 8];  target = 2
    print('Entrada:',arr,target)
    print('Saída : 6')
    print(countFreq(arr, target))
    print('countFreq \nExemplo 2 :')
    arr = [1, 3, 3, 4, 4,4,4, 7, 8, 8];  target = 8
    print('Entrada:',arr,target)
    print('Saída : 2')
    print(countFreq(arr, target))
    arr = [1, 3, 3, 4, 4,4,4, 7, 8, 8];  target = 9
    print('Entrada:',arr,target)
    print('Saída : 0')
    print(countFreq(arr, target))

def prob9():
    print('Search2DMatrix \nExemplo 1 :')
    matrix = [[1,3,5],[10,11,16],[23,30,34]]; target = 11
    print('Entrada: ', matrix, target)
    print('Saída: True ')
    if recursiveSearch2DMatrix(matrix,target):
        print("True")
    else:
        print("False")
    print('Exemplo 2 :')
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 13
    print('Entrada: ', matrix, target)
    print('Saída: False ')
    if recursiveSearch2DMatrix(matrix,target):
        print("True")
    else:
        print("False")

#prob0()
#prob1()
#prob2()
#prob3()
#prob4()
#prob5()
#prob6()    
#prob7()
#prob8()
prob9()