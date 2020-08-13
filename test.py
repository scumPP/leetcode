def isMatch(s,p):
    ##模式串p为空时，当s为空时匹配成功，当s不为空时匹配失败
    if not p:##p==''
        return not s
    ##s为空并且p只有一个字符时，匹配失败。为什么不是len(p)>1呢？假如p='a*' or p='.*'等情况，虽然p是两个字符，但是结果是匹配成功的
    if not s and len(p)==1:##not s等于s==''
        return False

    ##初始化dp矩阵，都为Flase，行和列各加1，因为要考虑空串的情况
    row=len(s)+1
    col=len(p)+1
    dp=[[False for _ in range(col)] for _ in range(row)]

    dp[0][0]=True  ##s和p都为空时，匹配成功
    dp[0][1]=False  ##s为空，p有一个字符时，匹配失败
    ##当s为空，p不为空但是匹配成功的情况
    for i in range(2,col):
        c=i-1
        if p[c]=='*':
            dp[0][i-2]=dp[0][i]

    ##开始遍历并且考虑其他各种情况
    for m in range(1,row):
        i=m-1
        for n in range(1,col):
            j=n-1
            ##最简单的情况，当前s字符与当前的p字符相等，或者当前p字符为'.'，即可以和任何字符匹配
            if s[i]==p[j] or p[j]=='.':
                dp[m][n]=dp[m-1][n-1]
            ##最复杂的情况，当p字符为'*'时，这时候匹配是否成功取决于'*'之前的字符和s当前字符的匹配情况
            elif p[j]=='*':
                ##'*'之前的字符和s当前字符相等，或者'*'之前的字符为万能字符'
                if p[j-1]==s[i] or p[j-1]=='.':
                    dp[i][j]=dp[i-1][j] or dp[i][j-2]
                else:
                    dp[i][j]=dp[i][j-2]   ##'*'之前的字符和s当前字符不相等时，此时匹配情况取决于p的j-2的匹配情况
            else:
                dp[i][j]=False
    return dp[row-1][col-1]


def sumFour(nums,target):
    if not nums and len(nums)>4:
        return []
    nums.sort()
    res=[]
    n=len(nums)
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            p=j+1
            q=n-1
            while p<q:
                if nums[i]+nums[j]+nums[p]+nums[q]>target:
                    q-=1
                    while nums[q]==nums[q-1]:
                        q-=1
                elif nums[i]+nums[j]+nums[p]+nums[q]<target:
                    p+=1
                    while nums[p]==nums[p+1]:
                        p+=1
                else:
                    res.append([nums[i],nums[j],nums[p],nums[q]])
                    while nums[q]==nums[q-1] and p<q:
                        q-=1
                    while nums[p]==nums[p+1] and p<q:
                        p+=1
                    p+=1
                    q-=1
    return res



if __name__ == "__main__":
    # s=''
    # p=''
    # print(isMatch(s,p))
    nums = [1, 0, -1, 0, -2, 2]
    res=sumFour(nums,0)
    print(res)