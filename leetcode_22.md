# 题目22:括号生成

题目：数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例：

```c++
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```

**思路**：

- 暴力递归解决：
   - 所有括号生成的组合可能有$2^{2n}$个，因此我们可以将所有可能的组合一一判断。
   - 在生成所有组合过程中，利用递归思想，共有m个符号的序列，这个序列取决于m-1个符号的序列加上一个“（”，或者一个“）”。
   - 生成完整的序列z后，判断z是否符合题目要求，即设置一个balance变量，遍历此时的z，字符为“（”，balance++；字符为“）”，balance--，最后balance为0，则为最后正确结果之一。

代码为：

```c++
bool isValid(const string& str){
    int balance=0;
    for(char s : str){
        if(s=='('){
            balance++;
        }else{
            balance--;
            if (balance<0){
                return false;
            }
        }
    }
    return balance==0;
}
void findValidCombi(string& curr_str,int n,vector<string>& res){
    if (n==curr_str.size()){
        if (isValid(curr_str)){
            res.push_back(curr_str);
        }
        return;
    }
    curr_str+='(';
    findValidCombi(curr_str,n,res);
    curr_str.pop_back();
    curr_str+=')';
    findValidCombi(curr_str,n,res);
    curr_str.pop_back();
}
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string cur_str;
        findValidCombi(curr_str,2*n,res);
        return res;
    }
```

- 回溯法
   - 回溯的出口：当序列z的字符个数等于2n
   - 核心还是递归，但是思想围绕“这个序列z不符合题目要求，那就退回去重新开始”的思想。
   - 怎么叫符合要求呢？就是当左括号的数目小于等于3，右括号的数目小于等于左括号的数目

代码如下：

```c++
void backtrack(vector<string>& ans, string& cur, int open, int close, int n) {
    if (cur.size() == n * 2) {
        ans.push_back(cur);
        return;
    }
    if (open < n) {
        cur.push_back('(');
        backtrack(ans, cur, open + 1, close, n);
        cur.pop_back();
    }
    if (close < open) {
        cur.push_back(')');
        backtrack(ans, cur, open, close + 1, n);
        cur.pop_back();
    }
}
vector<string> generateParenthesis(int n) {
    vector<string> result;
    string current;
    backtrack(result, current, 0, 0, n);
    return result;
}
```