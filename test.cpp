#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

int curr_div(int a,int b){
    if(a>b) return 0;
    int count=1;
    int temp=b;
    //此条件就是a-(temp+temp)>=0
    while(temp-a+temp>=0){
        count+=count;
        temp+=temp;
    }
    return count+curr_div(a-temp,b);
}
int divide(int dividend, int divisor) {
    //特殊情况
    if(dividend==0) return 0;
    if(divisor==1) return dividend;
    if(divisor==-1){
        if(dividend>INT_MIN) 
            return -dividend;
        return INT_MAX;
    }
    //记录结果的正负
    int sign=1;
    if((dividend>0 && divisor<0) || (dividend<0 && divisor>0))
        sign=-1;
    //都变成负数，防止溢出
    int a=dividend>0?-dividend:dividend;
    int b=divisor>0?-divisor:divisor;
    int res=curr_div(a,b);
    return sign==1?res:-res;
}

int main(){
    int dividend = 15;
    int divisor = 3;
    int res = divide(dividend,divisor);
    cout << res << endl;
}