#include <string>
#include <vector>
#include <queue>
#include <algorithm> // sort 사용을 위해 필요

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int time = 0; 
    int idx = 0; 
    int count = 0;
    
    sort(jobs.begin(), jobs.end());
    
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    
    while (count < jobs.size()) {
        
        while (idx < jobs.size() && jobs[idx][0] <= time) {
            pq.push({jobs[idx][1], jobs[idx][0], idx});
            idx++;
        }
        
        if (pq.empty()) {
            time = jobs[idx][0];
        } else {
            vector<int> current = pq.top();
            pq.pop();
            
            time += current[0];
            answer += (time - current[1]); 
            count++; 
        }
    }
    
    return answer / jobs.size();
}