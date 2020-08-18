# 字符串转换整数

题目：请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

- 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
- 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
- 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

**思想**：由于题目的限制条件很多，因此如果用常规方法的话，极大可能是不能100AC的，因此要使用“自动机”的方法

自动机，顾名思义就是自己主动解决问题，那么自己怎么解决呢？此时要引入状态，转移状态的概念。
先规定：

1. 当字符为空时，状态为start
2. 当字符为+或者-时，状态为sign
3. 当字符为数字时，状态为in_number
4. 当字符部位以上三种情况时，也就是字符不符合题目条件，状态结束，即为end

我们可以用以下的表格来进行解释：

|         |start|sign|in_number|end|
|---------|-----|----|---------|---|
|start    |start|sign|in_number|end|
|sign     |end  |end |in_number|end|
|in_number|end  |end |in_number|end|
|end      |end  |end |end      |end|

上面的表是状态转移的一个表，清晰地表示了自动机中每当字符的内容不同时的下一个状态。

具体代码为：

```c++
class Automation
{
    string state = "start";
    unordered_map<string, vector<string>> table = {
        {"start", {"start", "signed", "in_number", "end"}},
        {"signed", {"end", "end", "in_number", "end"}},
        {"in_number", {"end", "end", "in_number", "end"}},
        {"end", {"end", "end", "end", "end"}}};
    int get_col(char c)
    {
        if (isspace(c))
            return 0;
        if (c == '+' || c == '-')
            return 1;
        if (isdigit(c))
            return 2;
        return 3;
    }

public:
    int sign = 1;
    long long res = 0;
    void get(char c)
    {
        state = table[state][get_col(c)];
        if (state == "in_number")
        {
            res = res * 10 + c - '0';
            res = sign == 1 ? min(res, (long long)INT_MAX) : min(res, -(long long)INT_MIN);
        }
        else if (state == "signed")
        {
            sign = c == '+' ? 1 : -1;
        }
    }
};

int myAtomi(string str)
{
    Automation automation;
    for (char c : str)
    {
        automation.get(c);
    }
    return automation.sign * automation.res;
}
```