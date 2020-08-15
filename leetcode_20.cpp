#include <iostream>
#include <stack>
#include <stdio.h>
#include <vector>
using namespace std;

bool isOK(char temp1, char temp2)
{
    bool res = false;
    if (temp1 == '(' && temp2 == ')')
        res = true;
    if (temp1 == '{' && temp2 == '}')
        res = true;
    if (temp1 == '[' && temp2 == ']')
        res = true;
    return res;
}
bool isValid(string s)
{
    if(s=="")
        return true;
    stack<char> ss;
    int pos = 0;
    int n = s.size();
    while (pos < n)
    {
        if (s[pos] == '(' || s[pos] == '{' || s[pos] == '[')
        {
            ss.push(s[pos]);
        }
        if (s[pos] == ')' || s[pos] == '}' || s[pos] == ']')
        {
            if (!ss.empty())
            {
                char cur_char = ss.top();
                if (isOK(cur_char, s[pos]))
                {
                    ss.pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        pos++;
    }
    if (pos = n && ss.empty())
        return true;
    else
        return false;
}

int main()
{
    string s = "()";
    bool flag = isValid(s);
    cout << flag << endl;
}