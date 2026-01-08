#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_w = 0;
    int max_h = 0;
    int cw;
    int ch;
    vector<int> card;
    
    for (int i = 0; i < sizes.size(); i++) {
        card = sizes[i];
        
        if (card[0] < card[1]) {
            cw = card[1];
            ch = card[0];
        } else {
            cw = card[0];
            ch = card[1];
        }
        
        if (cw > max_w) {
            max_w = cw;
        }
        
        if (ch > max_h) {
            max_h = ch;
        }
    }
    
    return max_w*max_h;
}