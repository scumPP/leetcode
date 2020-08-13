def compute(num):
    num=str(num)
    cur_res=1
    for cur_num in num:
        cur_res*=int(cur_num)
    return cur_res

def convert(num,n):
    if n==1:
        return 0
    cur_res=compute(num)
    return convert(cur_res,len(str(cur_res)))+1 
    



if __name__ == "__main__":
    num=int(input())
    n=len(str(num))
    count=convert(num,n)
    print(count) 
