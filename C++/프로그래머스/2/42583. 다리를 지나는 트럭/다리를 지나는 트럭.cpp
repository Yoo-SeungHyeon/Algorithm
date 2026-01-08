#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int truck_idx = 0;
    int weight_sum = 0;
    queue<int> bridge;
    
    while (true) {
        answer++;
        
        if (bridge.size() == bridge_length) {
            weight_sum -= bridge.front();
            bridge.pop();
        }
        
        if (weight_sum + truck_weights[truck_idx] > weight) {
            bridge.push(0);
        } else {
            bridge.push(truck_weights[truck_idx]);
            weight_sum += truck_weights[truck_idx];
            truck_idx++;
        }
        
        if (truck_idx == truck_weights.size()){
            answer += bridge_length;
            break;
        }
    }   
    
    return answer;
}