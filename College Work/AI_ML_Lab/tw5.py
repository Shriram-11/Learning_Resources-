def minmax(node, tree, is_max_node):
    # Check if the current node is a leaf (no children)
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

    # Update the node's value with the computed minimax value
    tree[node][1] = value
    print(f"Node {node} computed value {value}")
    return value


# Provided tree structure
tree = {
    'A': [['B', 'C'], None],
    'B': [['D', 'E'], None],
    'C': [['F', 'G'], None],
    'D': [['H', 'I'], None],
    'E': [['J', 'K'], None],
    'F': [['L', 'M'], None],
    'G': [['N', 'O'], None],
    'H': [[], -1],
    'I': [[], 4],
    'J': [[], 3],
    'K': [[], 6],
    'L': [[], -3],
    'M': [[], -5],
    'N': [[], 0],
    'O': [[], 7]
}

# Starting the minimax algorithm from the root node 'A' assuming it's a max node
result = minmax('A', tree, True)
print(f"\nThe most appropriate value for the root node 'A' is {result}")
'''
Optional Part , i just did it to print a tree so that its easy for me to understand
Convert the tree to the format required by print_tree function
'''

def convert_tree(node_key, tree):
    node = {
        "value": f"{node_key} ({tree[node_key][1]})",
        "children": [convert_tree(child, tree) for child in tree[node_key][0]]
    }
    return node


# Convert the tree starting from root node 'A'
converted_tree = convert_tree('A', tree)

# Print the final tree with updated values


def print_tree(node, prefix="", is_tail=True):
    print(prefix + ("└── " if is_tail else "├── ") + str(node["value"]))
    for i, child in enumerate(node["children"]):
        print_tree(child, prefix + ("    " if is_tail else "│   "),
                   i == len(node["children"]) - 1)


print("\nFinal tree with updated values:")
print_tree(converted_tree)
