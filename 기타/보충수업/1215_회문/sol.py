import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    k = n//2
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8-n+1):
            # print(arr[i][j:j+n])
            # print(arr[i][j:j+n][::-1])  #이렇게도 가능하구나 ㅋㅋㅋㅋ
            # print('===========')
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                cnt += 1


    # arr2 = [[0]*8]*8        # 이 방법은 모든 행이 같은 객체를 참조한다고함.. 어쨌든 안되는 방식
    arr2 = [[0]*8 for _ in range(8)]        # 반드시 이 방법으로 입력!!!!
    for i in range(8):
        for j in range(8):
            arr2[i][j] = arr[j][i]      # 여기서도 반드시 arr2라는 새로운 행렬 생성


    # print('***************************')
    for i in range(8):
        for j in range(8 - n + 1):
            # print(arr2[i][j:j+n])
            # print(arr2[i][j:j+n][::-1])  #이렇게도 가능하구나 ㅋㅋㅋㅋ
            # print('===========')
            if arr2[i][j:j + n] == arr2[i][j:j + n][::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')


'''
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
'''