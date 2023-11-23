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
            pass


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5]
