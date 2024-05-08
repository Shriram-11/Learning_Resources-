import heapq


def astar(graph, start, goal):
    # priority queue to store nodes to be explored
    open_list = [(0, start)]
    # dictionary to store parent nodes
    parents = {}
    # dictionary to store g values (cost from start node to current node)
    g_values = {node: float('inf') for node in graph}
    g_values[start] = 0
    # dictionary to store f values (estimated total cost from start to goal)
    f_values = {node: float('inf') for node in graph}
    f_values[start] = graph[start][1]

    while open_list:
        # get node with minimum f value
        current_f, current_node = heapq.heappop(open_list)

        # check if current node is the goal
        if current_node == goal:
            path = []
            while current_node in parents:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            return path[::-1]

        # explore neighbors
        for child in graph[current_node][0]:
            # calculate tentative g value
            tentative_g = g_values[current_node] + graph[child][1]
            if tentative_g < g_values[child]:
                # update parent and g values
                parents[child] = current_node
                g_values[child] = tentative_g
                f_values[child] = tentative_g + graph[child][1]
                # add child to open list
                heapq.heappush(open_list, (f_values[child], child))

    # no path found
    return None


# Example usage:
start_node = 'A'
goal_node = 'M'
tree = {
    'A': [['B', 'C'], 30],
    'B': [['D', 'E', 'F'], 25],
    'C': [['G', 'H'], 28],
    'D': [['I'], 22],
    'E': [['J', 'K'], 19],
    'F': [[], 16],
    'G': [['L', 'M'], 10],
    'H': [['N'], 17],
    'I': [[], 9],
    'J': [[], 7],
    'K': [[], 6],
    'L': [[], 3],
    'M': [[], 0],
    'N': [[], 4]
}
path = astar(tree, start_node, goal_node)
print("Path:", path)
