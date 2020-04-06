# Z字形变换

这是一道medium的编程题,自己的思路不太对，就整理了别人的思路，flag用的太妙了！

## 题目如下：

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
例如
输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

```
L   C   I   R
E T O E S I I G
E   D   H   N
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

首先，我们来看输出的结果，对于行数为3的条件来说，结果可以分为三个部分，“LCIR”，“ETOESIIG”和“EDHN”，也就是说每一行为一部分，因此，我们在编程时，可以以行数作为条件初始化list。在这个例子中，就是初始化三个list，list1，list2，list3，分别存放“LCIR”，“ETOESIIG”和“EDHN”，即：

```
list1=['LCIR']
list2=['ETOESIIG']
list3=['EDHN']
```

然后，一个个输出的这种题目，一般情况下都会遍历输出，那么我们应该如何遍历，遍历谁呢？

这里呢，我们遍历输入的字符。因为从人的角度来看，当我们想转换Z字形时，我们是以想要转换的字符串为主，一个个按照规则转换的，因此在编程时，我们也利用这个思路，遍历要求转换的字符串，遍历过程中完成转换。

在我们按上面的思路来遍历的时候，行数会有这样一个规律，就是行数r从0,1,2...n，然后再从n,n-1,n-2,...,2,1。而且，当有这样一个变化时，是具备一定条件的，这种变化就是**转向**，导致这个**转向**的条件就是，行数r=0或者r=输入的行数，即最后一行。于是，我们引入了flag，巧妙地按照**转向**条件进行转换：
```
flag=-1
r=0
for c in s:
    re[r]+=c
    if r==0 or i==row-1:flag=-flag
    i+=flag

```
代码中r代表当前的行数，row代表要求转换的行数，完整代码就是：

```
def convert(self, s: str, numRows: int) -> str:
    if numRows<2:return s
    result=['' for _ in range(numRows)]
    flag=-1
    r=0
    for c in s:
        result[r]+=c
        if r==0 or r==numRows-1:
            flag=-flag
        r+=flag
    return ''.join(result)
```

