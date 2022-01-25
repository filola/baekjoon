# # 출력은 총 단지수 그리고 각 단지내 집의 수를 오름차순으로 정렬
# num = []
# count = 0

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def dfs(x,y, n, graph):
#     global count
#     if x < 0 or x >= n or y < 0 or y>=n:
#         return False

#     if graph[x][y] == 1:
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             dfs(x + dx[i], y + dy[i],n,graph)
#         return True

# def solution(n, graph):
#     global count
#     for i in range(n):
#         for j in range(n):
#             if dfs(i,j,n,graph) == True:
#                 num.append(count)
#                 count = 0
    
#     print(len(num))
#     num.sort()
#     for i in num:
#         print(i)

# solution(7,[[0,1,1,0,1,0,0],
# [0,1,1,0,1,0,1],
# [1,1,1,0,1,0,1],
# [0,0,0,0,1,1,1],
# [0,1,0,0,0,0,0],
# [0,1,1,1,1,1,0],
# [0,1,1,1,0,0,0]
# ])
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

num = []
count = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y, n, graph):
    global count
    if x < 0 or x >= n or y < 0 or y>=n:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i],n,graph)
        return True

def solution(n, graph):
    print(n, graph)
    global count
    for i in range(n):
        for j in range(n):
            if dfs(i,j,n,graph) == True:
                num.append(count)
                count = 0
    
    print(len(num))
    num.sort()
    for i in num:
        print(i)

solution(n,graph)