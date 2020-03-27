def cuttingRope(n: int) -> int:
        F=[0 for _ in range(n+1)]
        def memorize(n):
            if F[n]!=0:
                return F[n]
            if n==2:
                return 1
            re=-1
            for i in range(1,n):
                re=max(re,max(i*(n-i),i*memorize(n-i)))
            F[n]=re
            return re
        re=memorize(n)
        return re
print(cuttingRope(10))