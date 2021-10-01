import time
 
def merge(array, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = array[l + i] 
 
    for j in range(0 , n2): 
        R[j] = array[m + 1 + j] 
 
    i = 0    
    j = 0    
    k = l    
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            array[k] = L[i] 
            i += 1
        else: 
            array[k] = R[j] 
            j += 1
        k += 1
 
    while i < n1: 
        array[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        array[k] = R[j] 
        j += 1
        k += 1
 
def mergeSort(array,l,r): 
    if l < r: 
 
        m = (l+(r-1))//2
 
        mergeSort(array, l, m) 
        mergeSort(array, m+1, r) 
        merge(array, l, m, r) 
 
 
a1 = []
for i in range(0,2000):
    a1.append(i)
t1 = time.time()
mergeSort(a1, 0, len(a1) - 1) 
t2 = time.time()
print("--------------------------------------------------------------------")
 
print("Time for array with length 2000 is:  ", t2-t1) 
 
a2 = []
for i in range(0,4000):
    a2.append(i)
t3 = time.time()
mergeSort(a2, 0, len(a2) - 1) 
t4 = time.time()
print("--------------------------------------------------------------------")
 
print("Time for array with length 4000 is:  ", t4-t3) 
 
 
a3 = []
for i in range(0,6000):
    a3.append(i)
t5 = time.time()
mergeSort(a3, 0, len(a3) - 1) 
t6 = time.time()
print("--------------------------------------------------------------------")
 
print("Time for array with length 6000 is:  ", t6-t5) 
 
a4 = []
for i in range(0,8000):
    a4.append(i)
t7 = time.time()
mergeSort(a4, 0, len(a4) - 1) 
t8 = time.time()
print("--------------------------------------------------------------------")
 
print("Time for array with length 8000 is:  ", t8-t7) 
 
 
a5 = []
for i in range(0,10000):
    a5.append(i)
t9 = time.time()
mergeSort(a5, 0, len(a5) - 1) 
t10 = time.time()
print("--------------------------------------------------------------------")
 
print("Time for array with length 10000 is: ", t10-t9) 
 
print("--------------------------------------------------------------------")
