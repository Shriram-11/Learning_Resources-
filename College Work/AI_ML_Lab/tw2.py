tree = {
    'S': [['A', 'B'], 13],
    'A': [['C', 'D'], 12],
    'B': [['E', 'F'], 4],
    'E': [['H'], 8],
    'H': [[], 4],
    'F': [['I', 'G'], 2],
    'G': [[], 0],
    'I': [[], 9],
    'C': [[], 7],
    'D': [[], 3],
}


def get_start():
    max_value = -float('inf')  # Initialize max_value to a very small number
    start_node = ""

    for node in tree:
        if tree[node][1] > max_value:
            max_value = tree[node][1]
            start_node = node

    return start_node


def get_end():
    minv = float('inf')  # Initialize minv with a large number
    goal = ""

    for node in tree:
        if tree[node][1] < minv:
            minv = tree[node][1]
            goal = node

    return goal


start = get_start()
goal = get_end()

print("Start:", start, "\tEnd:", goal, "\n")


def get_children(node):
    children = tree[node][0]
    return [(child, tree[child][1]) for child in children]


def sort_queue(queue):
    return sorted(queue, key=lambda x: x[1])


def bfs(start):
    queue = [(start, tree[start][1])]
    path = []

    while queue:
        queue = sort_queue(queue)
        node, _ = queue.pop(0)

        path.append(node)
        print("Current Path:", path)

        if node == goal:
            return True, path

        children = get_children(node)
        for child, heuristic in children:
            queue.append((child, heuristic))

    return False, []


success, path = bfs(start)
if success:
    print("Goal reached. Path:", path)
else:
    print("Goal not reachable.")
