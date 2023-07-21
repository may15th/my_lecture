# index 접근 이라는 것을 할 수 있다.
# index 접근이란건... 어디에? list, str -> 순서가 있는 sequence 자료형
# 슬라이싱이란...?

#      0  1  2  3  4
#      |  |  |  |  |
list = [1, 2, 3, 4, 5]
print(list[1 : 4 : 1])  # [2, 3, 4] -> 왜 잘랏는데 값이 나오는지
print(list[1 : 4 : 2]) # [2, 4]
print(list[1 : 4 : 3]) # [2] -> 3칸 띄워서 잘랏으면 [2, 3] 만 나와야 하는 것 아닌가요
# 슬라이싱 쓸 때는 범위 벗어나도 오류 없이 잘 나오니까 주의하자.
# list[start : end : step] 
# | start에 작성한 내용은 그 index 번호 부터 시작,
# | end에 작성한 내용은 그 index-1 번째 까지 만 출력
# | step에 작성한 내용은, start 부터 end까지 step 만큼 건너 뛰면서
    # range(start, end, step)
print(list[1:100])