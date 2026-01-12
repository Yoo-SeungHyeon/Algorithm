#include <string>
#include <vector>

using namespace std;

// 재귀 함수에서 접근할 수 있도록 전역 변수로 선언
int answer = 0;
int cnt = 0;
string target = "";
string aeiou = "AEIOU";

void dfs(string str) {
    if (str == target) {
        answer = cnt;
        return;
    }

    if (str.length() >= 5) return;

    for (char s : aeiou) {
        if (answer != 0) return;

        cnt++;
        dfs(str + s);
    }
}

int solution(string word) {
    answer = 0;
    cnt = 0;
    target = word;
    
    dfs("");
    
    return answer;
}