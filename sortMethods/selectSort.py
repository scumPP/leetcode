def selectSort(alist):
    for i in range(len(alist)):
        min=i
        for j in range(i+1,len(alist)):
            if alist[j]<=alist[min]:
                min=j
        alist[i],alist[min]=alist[min],alist[i]
    return alist
                

if __name__=='__main__':
    a=[8,2,5,9,7]
    a1=selectSort(a)
    print(a1)