#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    // 각각의 수포자가 맞춘 정답의 수
    int supo1 = 0;
    int supo2 = 0;
    int supo3 = 0;
    
    // 각 수포자의 정답 패턴
    vector<int> supo1_var = {1,2,3,4,5};
    vector<int> supo2_var = {2,1,2,3,2,4,2,5};
    vector<int> supo3_var = {3,3,1,1,2,2,4,4,5,5};
    
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == supo1_var[i%5]) {
            supo1++;
        }
        if (answers[i] == supo2_var[i%8]) {
            supo2++;
        }
        if (answers[i] == supo3_var[i%10]) {
            supo3++;
        }
    }
    
    int max_score = max({supo1, supo2, supo3});
    
    if (supo1 == max_score) answer.push_back(1);
    if (supo2 == max_score) answer.push_back(2);
    if (supo3 == max_score) answer.push_back(3);
        
    return answer;
}