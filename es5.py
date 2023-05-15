class Graph:
    def __init__(self):
        self._nodes = {}

    def add_node(self, node: int) -> None:
        self._nodes[node] = set()    

    def connect(self, node_1: int, node_2: int) -> None:
        self._nodes[node_1].add(node_2)
        self._nodes[node_2].add(node_1)

    def are_connected(self, node_1: int, node_2: int) -> bool:
        return node_2 in self._nodes[node_1] 
    
    def find_path(self, node_1: int, node_2: int, recursive: bool = True) -> list[int]:
        if recursive:
            path = []
            visited = set()
            self._depth_first(node_1, node_2, path, visited)
        else:
            path = self._breadth_first(node_1, node_2)
        return path

    def _depth_first(self, current: int, end: int, path: list[int], visited: set[int]) -> bool:
        path.append(current)
        visited.add(current)
        if current == end:
            return True
        adjacent = {s for s in self._nodes[current] if s not in visited}
        for s in adjacent:
            if self._depth_first(s, end, path, visited):
                return True
        path.pop()
        return False
    
    def _breadth_first(self, start: int, end: int) -> list[int]:
        visited = set()
        if start == end:
            return [start]
        paths = [[start]]
        while paths:
            path = paths.pop(0)
            current = path[-1]
            adjacent = {s for s in self._nodes[current] if s not in visited}
            for s in adjacent:
                if s == end:
                    return path + [s]
                visited.add(s)
                paths.append(path + [s])                
        return []


def main():
    # creo un grafo con 10 nodi
    g = Graph()

    for i in range(10):
        g.add_node(i)

    # connetto i nodi
    g.connect(0, 2)
    g.connect(1, 2)
    g.connect(1, 3)
    g.connect(2, 3)
    g.connect(2, 5)
    g.connect(3, 4)
    g.connect(3, 6)
    g.connect(6, 8)
    g.connect(5, 8)
    g.connect(4, 9)
    g.connect(3, 9)
    g.connect(7, 2)

    print(g.find_path(7, 5))
    print(g.find_path(7, 5, recursive=False))


if __name__ == "__main__":
    main()