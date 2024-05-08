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

    iteration = 0

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
            final_cost = g_values[goal]
            print(f"\nFinal Cost: {final_cost}")
            return path[::-1]

        # explore neighbors
        for child, cost in graph[current_node][0].items():
            # calculate tentative g value
            tentative_g = g_values[current_node] + cost
            if tentative_g < g_values[child]:
                # update parent and g values
                parents[child] = current_node
                g_values[child] = tentative_g
                f_values[child] = tentative_g + graph[child][1]
                # add child to open list
                heapq.heappush(open_list, (f_values[child], child))

        iteration += 1
        print(f"\nIteration {iteration}:")
        print("Current Path:", reconstruct_path(parents, start, current_node))
        print(f"Evaluation Function Value for {
              current_node}: {f_values[current_node]}")


# Function to reconstruct the path from start to goal using parent nodes
def reconstruct_path(parents, start, goal):
    path = [goal]
    while goal != start:
        goal = parents[goal]
        path.append(goal)
    return path[::-1]


# Example usage:
start_node = 'A'
goal_node = 'G'
tree = {
    'A': [{'B': 5, 'C': 10}, 10],
    'B': [{'D': 5, 'E': 5}, 7],
    'C': [{'F': 5}, 7],
    'D': [{'G': 10}, 3],
    'E': [{'G': 7}, 2],
    'F': [{'G': 8}, 1],
    'G': [{}, 0]
}


def print_tree(node, graph, prefix="", is_tail=True):
    neighbors, heuristic = graph[node]
    print(prefix + ("└── " if is_tail else "├── ") + f"{node} (h={heuristic})")
    if neighbors:
        for neighbor, cost in neighbors.items():
            print_tree(neighbor, graph, prefix +
                       ("    " if is_tail else "│   ") + f"(cost={cost}) ", neighbor == list(neighbors.keys())[-1])


# Example usage:
print("Tree with Heuristics and Costs:")
print_tree(start_node, tree)

print("\nA* Search Path:")
path = astar(tree, start_node, goal_node)
print("Final Path:", path)
