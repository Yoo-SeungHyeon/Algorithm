#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    int left = 0;
    int right = 0;
    
    for (char c : s) {
        if (c == '(') {
            left++;
        } else {
            right++;
        }
        
        if (left < right) {
            answer = false;
            break;
        }
    }
    if (left != right) {
        answer = false;
    }
    
    return answer;
}