#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    int v_size = progresses.size();
    
    vector<int> temp;
    
    for (int i = 0; i < v_size; i++){
        int l_progress = (100 - progresses[i]);
        int days;
        
        if (l_progress % speeds[i]) {
            days = l_progress / speeds[i] + 1;
        } else {
            days = l_progress / speeds[i];
        }
        
        temp.push_back(days);
    }
    
    int max_num = 0;
    int count = 0;
    
    for (int num : temp){
        if (max_num >= num) {
            count++;
        } else {
            max_num = num;
            answer.push_back(count);
            count = 1;
        }
    }
    answer.push_back(count);
    
    answer.erase(answer.begin());
    
    return answer;
}