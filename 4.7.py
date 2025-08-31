from collections import deque

def findBuildOrder(projects, dependencies):
    g = {}
    edges = {}
    for project in projects:
        g[project] = []
        edges[project] = 0
    for u,v in dependencies:
        g[u].append(v)
        edges[v] += 1
    n = deque([e for e in edges if edges[e] == 0])
    bo = []
    while n:
        curr = n.popleft()
        bo.append(curr)
        for e in g[curr]:
            edges[e] -= 1
            if edges[e] == 0:
                n.append(e)
    if len(bo) != len(projects):
        raise Exception(f"expected {len(projects)} projects, got {len(bo)}")
    return bo


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
print(findBuildOrder(projects, dependencies))

# projects = ["a", "b", "c"]
# dependencies = [("c", "a"), ("a", "b"), ("b", "a")]
# print(findBuildOrder(projects, dependencies))

a,b,c,d,e,f,g = "a", "b", "c", "d", "e", "f", "g"
projects = ["a", "b", "c", "d", "e", "f", g]
dependencies = [(f,c), (f,b), (f,a), (c,a), (b,a), (b,e), (a,e), (d,g)]
print(findBuildOrder(projects, dependencies))




