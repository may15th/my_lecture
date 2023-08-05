#arr: 원본 배열
#N : 배열의 길이
#key : 타겟
def binary_search(arr,N, key, start, end):
    if start > end: #시작지점이 끝지점보다 커지면 # 타겟 찾을 수 없음 조사 종료
        return False
    else:
        mid = (start+end)//2 #중앙 인덱스 
        print(mid,arr[mid])
        #중앙 위치가 내가 찾는 대상이라면
        if arr[mid] == key:
            return True
        #아닌데, 중앙 위치값이 내 키 값보다 크면
        elif arr[mid] > key:
            end = mid-1
            return binary_search(arr,N,key,start,end)
        # 아닌데, 중앙 위치값이 내 키값보다 작으면
        else:
            start = mid +1
            return binary_search(arr,N,key,start,end)
            pass
    return False

numbers = list(range(1, 30, 2))
print(numbers)
N = len(numbers)
target = 25
#이진 탐색 
print(binary_search(numbers,N,target,0, N-1)) #numbers, N, target 인자 들어가는거 당연하다...