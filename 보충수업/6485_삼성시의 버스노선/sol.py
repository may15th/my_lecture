import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai, Bi = map(int(input()))
    bus_stop = [0] * 5001
    for i in range(Ai, Bi+1):
        bus_stop[i] = 1

    P = int(input())
    for j in range(1, P+1):
        Cj = int(input())




    print(f'#{tc}', end = ' ')
    print()