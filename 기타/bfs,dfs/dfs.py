def dfs(start):
    roote.append(start)
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)


arr = [[],[2,3,4],[1,4],[1,4],[1,2,3]]
visited = [0,0,0,0,0]
roote = []
dfs(1)
print(roote)

