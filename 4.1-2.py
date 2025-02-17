from collections import deque

def bfs(start, end, g):
    v = set()
    q = deque()
    q.append(start)
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in v:
                continue
            v.add(curr)
            if curr == end:
                return True
            for child in g[curr]:
                if child not in v:
                    q.append(child)
    return False

adjList = {
    1:[2,7],
    2:[3,5,7],
    3:[4,5],
    4:[6,9],
    5:[],
    6:[3],
    7:[],
    8:[1,2,5],
    9:[3,5]
}

print(bfs(1,4,adjList))
print(bfs(4,1,adjList))