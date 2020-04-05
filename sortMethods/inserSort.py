def insertSort(alist):
    n=len(alist)
    for i in range(1,n):
        value=alist[i]
        insert_index=-1
        for j in range(i-1,-1,-1):
            if alist[j]>value:
                alist[j+1]=alist[j]
                insert_index=j
            else:
                break
        if insert_index!=-1:
            alist[insert_index]=value
    return alist


if __name__=='__main__':
    a=[8,2,5,9,7]
    a1=insertSort(a)
    print(a1)
