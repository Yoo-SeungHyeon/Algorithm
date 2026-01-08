#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    // 1. {우선순위, 초기 인덱스}를 쌍으로 저장하는 큐 생성
    queue<pair<int, int>> q;
    
    // 2. 우선순위 비교를 위해 내림차순 정렬된 우선순위 큐 생성
    priority_queue<int> pq;

    for (int i = 0; i < priorities.size(); i++) {
        q.push({priorities[i], i});
        pq.push(priorities[i]);
    }

    while (!q.empty()) {
        int current_p = q.front().first;
        int current_idx = q.front().second;
        q.pop();

        // 현재 문서의 중요도가 가장 높은 중요도(pq.top)와 같다면 인쇄
        if (current_p == pq.top()) {
            pq.pop(); // 인쇄했으므로 최대 중요도 목록에서 제거
            answer++; // 인쇄 순서 증가

            // 우리가 찾는 문서라면 결과 반환
            if (current_idx == location) {
                return answer;
            }
        } 
        // 중요도가 더 높은 문서가 있다면 뒤로 보냄
        else {
            q.push({current_p, current_idx});
        }
    }

    return answer;
}