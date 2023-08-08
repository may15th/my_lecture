import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    str1_dict = {}  # 동일한 문자의 수를 세기 위한 dictionary 생성

    # 짧은 문자열을 돌면서 딕셔너리에 추가(알파벳 :0)
    for i in range(len(str1)):
        str1_dict[str1[i]] = 0

    # 짧은 문자열의 알파벳과 긴 문자열의 알파벳이 같으면 cnt +1
    for i in range(len(str1)):
        val_cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                val_cnt += 1
            str1_dict[str1[i]] = val_cnt

    max_cnt = 0
    for i in range(len(str1)):
        if max_cnt < str1_dict.get(str1[i]):
            max_cnt = str1_dict.get(str1[i])

    print(f'#{tc} {max_cnt}')