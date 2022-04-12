def BFS_SP(graph, start, goal):
    all_paths = []
    explored = []
     
    queue = [[start]]
     
    if start == goal:
        print("Same Node")
        return
     
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    all_paths.append(new_path)
            explored.append(node)
    
    print(all_paths)
    smallest_path_length = len(graph)
    for path in all_paths:

    return

graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
     
# Function Call

graph = {'0,0': ['0,1', '1,0'], '0,1': ['0,0', '0,2'], '0,2': ['0,1', '1,2'], '1,0': ['0,0', '2,0'], '1,2': ['0,2', '2,2'], '2,0': ['2,1', '1,0'], '2,1': ['2,0', '2,2'], '2,2': ['2,1', '1,2']}
a = BFS_SP(graph, '0,0', '1,2')
print(a)