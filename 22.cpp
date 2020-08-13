#include <string>
#include <vector> 
#include <iostream> 
using namespace std;

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

int main(){
    vector<string> combis=generateParenthesis(3);
    for (vector<string>::iterator it = combis.begin(); it != combis.end();it++){
        cout<<*it<<" "<<endl;
    }
    return 0;
}
