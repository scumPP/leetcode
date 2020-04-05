
def partion(alist,start,end):
    base=alist[start]
    low=start
    high=end

    while low<high:
        while alist[high]>=base and low<high:
            high-=1
        alist[low]=alist[high]
        while alist[low]<=base and low<high:
            low+=1
        alist[high]=alist[low]
        alist[low]=base
    return low

def quickSort(alist,start,end):
    if start<end:
        p=partion(alist,start,end)
        quickSort(alist,start,p-1)
        quickSort(alist,p+1,end)
    return alist
        


if __name__ == "__main__":
    s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    print("before sort:",s)
    s1 = quickSort(s, 0, len(s) - 1)
    print("after sort:",s1)