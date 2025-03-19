import math

global NOT_FOUND
NOT_FOUND=-1

# iterative find (unordered array)
def find(alist,key):
  N = len(alist)
  for i in range(0, N):
       if key == alist[i]:
          return i   
  return NOT_FOUND

"""  ordered array """
# iterative scan search 
def scan(alist,key):
  N = len(alist)
  for i in range(0, N):
       if key == alist[i]:
          return i
       elif key < alist[i]:
          return NOT_FOUND        
  return NOT_FOUND

# recursive scanner search - another way 
def recursiveScan(alist,key):
  def body(alist,key,i):
    N = len(alist)
    if i == N:
      return NOT_FOUND        
    elif key == alist[i]:
      return i
    elif key < alist[i]:
      return NOT_FOUND        
    return body(alist,key,i+1)
  return body(alist,key,0)


# iterative binary search
def iterativeBinarySearch(alist,key):
  N = len(alist)  
  low = 0
  high = N-1
  mid=(low+high) //2
  while(low <= high):
     if key == alist[mid]:
        return mid
     elif key < alist[mid]:
        high=mid-1
     else:
        low=mid+1
     mid=(low+high) //2
  return NOT_FOUND

# recursive binary search
def recursiveBinarySearch(alist,key):
  def body(alist,key,low,high):
      mid=(low+high) //2
      if low > high:
        return NOT_FOUND    
      elif key == alist[mid]:
        return mid
      elif key < alist[mid]:
        return body(alist,key,low,mid-1)
      else:
        return body(alist,key,mid+1,high)
  return body(alist,key,0,len(alist)-1)

#
# Esta função só vale para chaves numéricas
#  
# interative interpolation search
def iterativeInterpolationSearch(alist,key):
    N = len(alist);  low=0; high=N-1
    while(low <= high):
        min = alist[low];  max = alist[high]
        mid = ( low + abs((high-low ) * (key-min))// (max-min))
        print(mid)
        if(max==min):
          return NOT_FOUND
        elif(mid>high or mid<low):
          return NOT_FOUND
        elif( alist[ mid ]== key ):
          return mid
        elif( alist[ mid ] < key ):
          low= mid + 1
        else : 
          high=mid - 1
    return NOT_FOUND

#
# Esta função só vale para chaves numéricas
#
# recursive interpolation search
def recursiveInterpolationSearch(alist,key):
  def body(alist,key,low,high):
    if(low<=high):
        min = alist[low]; max = alist[high]
        mid = ( low + abs((high-low ) * (key-min))// (max-min))    
        if(max==min):
          return NOT_FOUND
        elif(mid>high or mid<low):
          return NOT_FOUND
        elif( alist[ mid ] == key ):
          return mid
        elif( alist[ mid ] < key ):
          return body(alist,key,mid+1,high)
        else : 
          return body(alist,key,low,mid-1)
    else:
          return NOT_FOUND
  return body(alist,key,0,len(alist)-1)


# iterative blocked search with blockScan
def iterativeBlockedSearch(alist,key):
  def blockScan(key,alist,min,max):
    for i in range(min,max):      
      if key == alist[i]:
        return i
      if key < alist[i]:
        return NOT_FOUND
    return NOT_FOUND
  """main """
  N = len(alist)
  block_size= int(math.sqrt(N))  # tamanho lógico do bloco
  for bn in range(0,N // block_size + 1):  # pesquisa do bloco 
    # bn : número do bloco: 0,1,2, ....   
    # inicializa i com o índice da primeira célula do bloco 
    i=block_size*(bn+1)-1 
    if(i >= N): # verifica se índice é maior índice da última célula
      i = N - 1 # retorna i para a posição final do vetor
    elif key > alist[i]: # chave maior que a última chave do bloco 
        if i == N - 1 :
          return NOT_FOUND
        else:
          continue
    else:
        # percorre o bloco que pode conter a chave                
        return blockScan(key,alist,bn*block_size,i+1)

# iterative blocked search with binary search
def iterativeBlockedSearchBS(alist,key):
  def body(alist,key,low,high):
      mid=(low+high) // 2    
      if low > high:
        return NOT_FOUND    
      elif key == alist[mid]:
        return mid
      elif key < alist[mid]:
        return body(alist,key,low,mid-1)
      else:
        return body(alist,key,mid+1,high)
  
  N = len(alist)
  block_size= int(math.sqrt(N))  # tamanho lógico do bloco
  for bn in range(0,N // block_size + 1):  # pesquisa do bloco 
    # bn : número do bloco: 0,1,2, ....   
    # inicializa i com o índice da primeira célula do bloco 
    i=block_size*(bn+1)-1 
    if(i >= N): # verifica se índice é maior índice da última célula
      i = N - 1 # retorna i para a posição final do vetor
    elif key > alist[i]: # chave maior que a última chave do bloco 
        if i == N - 1 :
          return NOT_FOUND
        else:
          continue
    else:
        # percorre o bloco que pode conter a chave                
        return body(alist,key,bn*block_size,i+1)

def blockedBinarySearch(arr, key):
    # auxiliary recursiveBinarySearch
    def recursiveBinarySearch(alist,key,low,high):
      mid=(low+high) //2    
      if low > high:
        return NOT_FOUND    
      elif key == alist[mid]:
        return mid
      elif key < alist[mid]:
        return recursiveBinarySearch(alist,key,low,mid-1)
      else:
        return recursiveBinarySearch(alist,key,mid+1,high)
      
    # recursive body blockedBinarySearch     
    def body(alist, block_size, low, high, key): 
        mid=(low+high) // 2
        if low > high or block_size*(mid+1) > len(alist)-1:
            return NOT_FOUND
        elif key < alist[block_size*mid]:
            return body(alist,block_size,low,mid-1,key)
        elif key > alist[block_size*(mid+1)]:
            return body(alist,block_size,mid+1,high,key)    
        else:
            pos = recursiveBinarySearch(alist,key,block_size*mid,block_size*(mid+1))
            if pos == -1:
                return NOT_FOUND
            else:
                return pos # pos+block_size*mid

    block_size= int(math.sqrt(len(arr)))   # tamanho lógico do bloco
    return body(arr,block_size,0, len(arr) // block_size, key)

if __name__ == '__main__':
   arr=[10, 15, 20, 35, 50, 65, 70, 80, 90, 95];key=15
   while True:
          print(arr)
          print("Escolha uma opção:\n1- scan\n2- recursive scan")
          print("3 - iterative binary search\n4- recursive binary search\n5- iterative interpolation search")
          print("6- recursive interpolation search\n7- Sair")
          opcao = int(input())
          if opcao < 1 or opcao > 7:
            continue
          if opcao == 7:  break
          key=int(input('digite a chave de pesquisa : '))
          if opcao == 1:
            print('scan ',scan(arr,key))
          elif opcao == 2:
            print('recscan ',recursiveScan(arr,key))
          elif opcao == 3:
            print('iterative binary search ',iterativeBinarySearch(arr,key))
          elif opcao == 4:
            print('recursive binary search ',recursiveBinarySearch(arr,key))
          elif opcao == 5:
            print('iterative interpolation search ',iterativeInterpolationSearch(arr,key))
          else:
            print('recursive inter search ',recursiveInterpolationSearch(arr,key))
          input()
##
#print('iterative block search ',iterativeBlockedSearch(arr,key))
#print('recursive block binary search ',iterativeBlockedSearchBS(arr,key))
#print('recursive block binary search ',blockedBinarySearch(arr,key))
