

visited = [0]

G = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
n = len(G)
visited = [0] * (n+1)
start = []
end = []
for i in G:
    if i % 2 ==0:
        start.append(i)
    else:
        end.append(i)

start