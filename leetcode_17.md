# LC 17 电话号码的字母组合

题目：给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

对应按键如下:

```c++
map<char,string> numbers_letters={
        {'2',"abc"},
        {'3',"def"},
        {'4',"ghi"},
        {'5',"jkl"},
        {'6',"mno"},
        {'7',"pqrs"},
        {'8',"tuv"},
        {'9',"wxyz"},
    };
```

示例：

```c++
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

思路：排列组合，回溯法解决。

- 出口是如果当前的字母组合数目等于给定的字符串的数目，即为最后结果之一

- 回溯本质还是遍历所有的可能，所以这里利用递归+循环来遍历所有可能的字母组合，需要注意的是递归函数中的有些参数是需要做改变的

具体代码如下：

```c++
    vector<string> letterCombinations(string digits) {
        if (digits.size()==0){
            return res;
        }
        backtrack(digits,digits.size(),0);
        return res;
    }

    vector<string> res;
    map<char,string> numbers_letters={
        {'2',"abc"},
        {'3',"def"},
        {'4',"ghi"},
        {'5',"jkl"},
        {'6',"mno"},
        {'7',"pqrs"},
        {'8',"tuv"},
        {'9',"wxyz"},
    };
    string s;
    void backtrack(string digits,int count,int index){
        if(s.size()==count){
            res.push_back(s);
            return; 
        }
        for(int i=0;i<numbers_letters[digits[index]].size();i++){
            s+=numbers_letters[digits[index]][i];
            backtrack(digits,digits.size(),index+1);
            s.pop_back();
        }
    }
```