def bubbleSort(alist):
    n=len(alist)
    for i in range(n):
        for j in range(n):
            if alist[i]<=alist[j]:
                alist[j],alist[i]=alist[i],alist[j]
    return alist

if __name__=='__main__':
    a=[8,2,5,9,7]
    a1=bubbleSort(a)
    print(a1)
