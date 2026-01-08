#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    // 노란색의 넓이 = yw * yh
    // 갈색의 둘레 갯수 = (yw+yh + 2)*2
    // 조건 가로 > 세로
    
    for (int x = 1; x*x < yellow + 1; x ++) {
        if (yellow % x == 0) {
            int y = yellow/x;
            if (brown == 2*(x + y + 2)) {
                if (x < y) {
                    answer = {y+2, x + 2};
                    break;
                } else {
                    answer = {x + 2, y + 2};
                    break;
                }
            }
        }
    }
    
    return answer;
}