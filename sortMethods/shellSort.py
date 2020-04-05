def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            while i >= gap and arr[i] < arr[i - gap]:
                arr[i], arr[i - gap] = arr[i - gap], arr[i]
                i -= gap
                #print(arr)
        gap //= 2
    return arr

re=shellSort([2,4,8,1,5,0,6])

print(re)
