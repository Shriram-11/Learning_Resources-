def iterative_deepening_dfs(start, target, max_depth):
    depth = 0
    print("Depth: ", depth)
    bottom_reached = False
    while not bottom_reached and depth <= max_depth:
        result, path, bottom_reached = iterative_deepening_dfs_rec(
            start, target, 0, depth, [])
        if result is not None:
            return result
        depth += 1
        print("Increasing depth to " + str(depth), "\n")
    return None


def iterative_deepening_dfs_rec(node, target, current_depth, max_depth, path):
    print("Visiting Node " + str(node["value"]))
    if node["value"] == target:
        print("Found the node we're looking for!")
        return node, path, True
    if current_depth == max_depth:
        if len(node["children"]) > 0:
            return None, path, False
        else:
            return None, path, True
    bottom_reached = True
    for i in range(len(node["children"])):
        result, path_copy, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1,
                                                                            max_depth, path + [node["value"]])
        if result is not None:
            return result, path_copy, True
        bottom_reached = bottom_reached and bottom_reached_rec
    return None, path, bottom_reached


def print_tree(node, prefix="", is_tail=True):
    print(prefix + ("└── " if is_tail else "├── ") + str(node["value"]))
    if node["children"]:
        for i, child in enumerate(node["children"]):
            print_tree(child, prefix + ("    " if is_tail else "│   "),
                       i == len(node["children"]) - 1)


tree = {
    "value": 1,
    "children": [
        {
            "value": 2,
            "children": [
                {"value": 5, "children": []},
                {"value": 6, "children": []}
            ]
        },
        {
            "value": 3,
            "children": [
                {"value": 7, "children": []},
                {"value": 8, "children": []}
            ]
        },
        {
            "value": 4,
            "children": [
                {"value": 9, "children": []},
                {"value": 10, "children": []}
            ]
        }
    ]
}

print("\nTree structure:")
print_tree(tree)

target_value = 10
print("\nTarget node:", target_value)

max_depth = 2
print("\n Max depth:", max_depth)
result_node = iterative_deepening_dfs(tree, target_value, max_depth)
if result_node:
    print("\nTarget node found:", result_node["value"])
else:
    print("\nTarget node not found in the tree.")
