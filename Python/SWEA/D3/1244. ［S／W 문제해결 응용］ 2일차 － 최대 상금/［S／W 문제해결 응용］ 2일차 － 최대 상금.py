# DFS로 모든 조합 찾기
def DFS(result, target, n, history):
    if n == 0:
        result.add(target)
        return

    # target과 n의 조합이 이미 탐색된 경우, 더 이상 진행하지 않음
    if (target, n) in history:
        return
    else:
        history.add((target, n))  # 조합을 history에 추가하여 중복 방지

    target_list = list(target)  # 문자열을 리스트로 변환하여 조작 가능하도록 함
    for i in range(len(target_list)):
        for j in range(i + 1, len(target_list)):
            target_list[i], target_list[j] = target_list[j], target_list[i]  # 두 자리를 바꿈
            DFS(result, ''.join(target_list), n - 1, history)  # 재귀 호출
            target_list[i], target_list[j] = target_list[j], target_list[i]  # 다시 원상복구
    return result


T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    num, chan = input().split()  # num: 숫자, chan: 교환 횟수
    chance = int(chan)  # 기회 횟수
    result = set()  # 가능한 모든 숫자를 저장할 set
    history = set()  # DFS에서 중복을 피할 history set
    results = DFS(result, num, chance, history)  # DFS로 모든 경우의 수 찾기
    print(f'#{tc} {max(results)}')  # 결과 출력 (최댓값)
