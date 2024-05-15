def build_tree(node, levels):
    if levels == 0:
        return [[], None]
    children = [f"{node}{chr(65 + i)}" for i in range(2)]
    return [children, None]


def build_tree_recursively(tree, node, levels):
    if levels > 0:
        tree[node] = build_tree(node, levels - 1)
        for child in tree[node][0]:
            build_tree_recursively(tree, child, levels - 1)


def get_leaf_nodes(tree):
    leaf_nodes = []
    for node in tree:
        if not tree[node][0]:  # No children
            leaf_nodes.append(node)
    return leaf_nodes


def input_leaf_values(tree):
    leaf_nodes = get_leaf_nodes(tree)
    for leaf in leaf_nodes:
        value = int(input(f"Enter value for leaf node {leaf}: "))
        tree[leaf][1] = value

# Adapted functions for Minimax algorithm


def minmax(node, tree, is_max_node):
    if len(tree[node][0]) == 0:
        print(f"Leaf node {node} has value {tree[node][1]}")
        return tree[node][1]

    children = tree[node][0]

    if is_max_node:
        value = -float('inf')
        print(f"Max node {node} with children {children}")
        for child in children:
            value = max(value, minmax(child, tree, False))
    else:
        value = float('inf')
        print(f"Min node {node} with children {children}")
        for child in children:
            value = min(value, minmax(child, tree, True))

    tree[node][1] = value
    print(f"Node {node} computed value {value}")
    return value

# Convert tree function


def convert_tree(node_key, tree):
    node = {
        "value": tree[node_key][1],
        "children": [convert_tree(child, tree) for child in tree[node_key][0]]
    }
    return node

# Print tree function


def print_tree(node, prefix="", is_tail=True):
    print(prefix + ("└───── " if is_tail else "├───── ") + str(node["value"]))
    for i, child in enumerate(node["children"]):
        print_tree(child, prefix + ("    " if is_tail else "│   "),
                   i == len(node["children"]) - 1)


# Main execution
levels = int(input("Enter the number of levels in the tree: "))
root = 'A'
tree = {}
build_tree_recursively(tree, root, levels)
input_leaf_values(tree)
result = minmax(root, tree, True)
print(f"\nThe most appropriate value for the root node '{root}' is {result}")

# Convert and print the final tree with updated values
converted_tree = convert_tree(root, tree)
print("\nFinal tree with updated values:")
print_tree(converted_tree)
