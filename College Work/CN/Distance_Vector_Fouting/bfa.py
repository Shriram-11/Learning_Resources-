import sys


class Network:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        self.distance_vector = {}

    def add_link(self, n1, n2, cost):
        if n1 not in self.graph:
            self.graph[n1] = {}
        self.graph[n1][n2] = cost

        if n2 not in self.graph:
            self.graph[n2] = {}
        self.graph[n2][n1] = cost

    def initialize_distance_vector(self, node):
        self.distance_vector[node] = {node: 0}
        for n in self.nodes:
            if n != node:
                self.distance_vector[node][n] = sys.maxsize

    def update_distance_vector(self, node):
        for dest in self.nodes:
            if dest != node:
                min_cost = sys.maxsize
                for neighbour in self.graph[node]:
                    if dest in self.distance_vector[neighbour]:
                        cost = self.distance_vector[neighbour][dest] + \
                            self.graph[node][neighbour]
                        min_cost = min(min_cost, cost)
                self.distance_vector[node][dest] = min_cost

    def print_routing_table(self, node):

        print(f"Routing table for Node:{node}\nDestination\t\tCost")
        for dest, cost in self.distance_vector[node].items():
            if dest != node:
                print(f"{dest}\t\t{cost}\n")


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5]
    net = Network(nodes)
    net.add_link(1, 2, 2)
    net.add_link(1, 3, 2)
    net.add_link(1, 4, 1)
    net.add_link(2, 3, 3)
    net.add_link(2, 5, 1)
    net.add_link(3, 4, 4)
    net.add_link(3, 5, 1)

    for node in nodes:
        net.initialize_distance_vector(node)
    for _ in range(6):
        for node in nodes:
            net.update_distance_vector(node)
    for node in nodes:
        net.print_routing_table(node)
