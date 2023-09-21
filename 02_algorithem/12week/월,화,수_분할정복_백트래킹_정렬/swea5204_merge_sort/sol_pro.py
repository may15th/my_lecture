import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    def merge_sort(left, right, arr):
        # 분할 종료 시점
        if len(arr) <=1:
            return arr

        # 중앙 위치
        mid = len(arr)//2

        # L[0:N//2], L[N//2:N]
        left = arr[:mid]
        right = arr[mid:]

        # 분할 종료 시점이 될 때까지 계속 쪼개기
        left = merge_sort(left)
        right = merge_sort(right)

        # 분할 온료 후, 병합하기 위한 과정

        # 왼쪽 리스트의 0번 인덱스와
        # 오른쪽 리스트의 0번 인덱스 값 비교
        # 그 중, 작은 값을 (오름차수 정렬 하니까) 먼저 어딘가에 담거나,원본에 넣거나
        left_index, right_index, k = 0,0,0
        # 좌, 우 정렬 시도


        # K => 원본에서 교체 되어야 될 위치
        while left_index < len(left) and right_index < len(right):
            # 오른쪽이 더 크면
            if left[left_index] < right[right_index]:
                # 원본 배여르이 k번째에 더 작은 값이 left 삽입
                arr[k] = left[left_index]
                left_index += 1
            # 왼쪽이 더 크면
            else:
                #원본 배열의 k번쨰에 더 작은 값인 right 삽입
                arr[k] = right[right_index]
                right_index += 1
            # 다음 원본 조사 위치로 이동
            k += 1

        # 모든 조사 완료 후, 아직 남아 있는 값 있을 수 있다.
        # 남아 있는 요소는
        if left_index < len(left):
            arr[k:] = left[left_index:]
        if right_index < len(right):
            arr[k:] = left[right_index:]

        return arr


    N = int(input())
    arr = list(map(int, input().split()))

    # N개의 정렬 대상을 가진 리스트 l을 분할할 때 L[0:N//2], L[N//2:N]으로 분할한다.
    # 병합 과정에서 다음
    result = 0
    arr = merge_sort(arr)
    print(f'#{tc}, {ans}')



    # 새 리스트 만들어서 병합 소트 하는 건 메모리를 많이 잡아먹는다.
    # 그래서 다른 방법이라는데 이해를 못함 ㅋㅋㅋㅋ

    