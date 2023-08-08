import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input)
    p = input()
    t = input()





    #최종 결과값
    result = 0
    p_idx = 0
    for t_idx in range(len(t) - len(p) + 1):
        if p_idx and t_idx + p_idx <= last_t_idx + len(p):
            continue

        for p_idx in range(len(p)):
            # 패턴과 타겟이 동일하지 않은 경우 한번이라도 나오면 조사 종료
            if p[p_idx] != t[t_idx + p_idx]:
                last_t_idx = t_idx
                p_idx = 0
                break

        else: # for 문도 else가 있다 :break된 적 없이 모두 순회했을때,
            result += 1
            last_t_idx = t_idx

    print(result)