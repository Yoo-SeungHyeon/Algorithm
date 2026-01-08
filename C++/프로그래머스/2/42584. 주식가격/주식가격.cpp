#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    //    pair<val, idx>
    queue<pair<int,int>> keep;
    
    for (int i = 0; i < prices.size(); i++) {
        queue<pair<int,int>> temp;
        
        while (!keep.empty()) {
            int val = keep.front().first;
            int idx = keep.front().second;
            keep.pop();
            
            answer[idx]++;
            
            if (val <= prices[i]) {
                temp.push({val, idx});
            }
        }
        keep = temp;
        keep.push({prices[i], i});
    }
    
    return answer;
}