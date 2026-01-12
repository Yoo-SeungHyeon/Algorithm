#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());    
    
    int min_scov1 = 0;
    int min_scov2 = 0;
        
    while (pq.top() < K) {
        
        if (pq.size() < 2) {
            return -1;
        }
        
        min_scov1 = pq.top();
        pq.pop();
        min_scov2 = pq.top();
        pq.pop();
        
        pq.push(min_scov1 + 2*min_scov2);
        answer++;
    }
    
    
    return answer;
}