#include <map>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> letterCombinations(string digits);
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
vector<string> res;
int main(){
    vector<string> res;
    res = letterCombinations("23");
    for (int i = 0; i < res.size();i++){
        cout << res[i] << endl;
    }      
}

void backtrack(string digits,int count,int index){
    if (s.size()==count){
        res.push_back(s);
        return;
    }
    
    for (int i = 0; i < numbers_letters[digits[index]].size();i++){
        s += numbers_letters[digits[index]];
        backtrack(digits, digits.size(), index + 1);
        s.pop_back();
    }
}
vector<string> letterCombinations(string digits){
    if(digits.size()==0){
        return res;
    }
    backtrack(digits,digits.size(),0);
    return res;
}