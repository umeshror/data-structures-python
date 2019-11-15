class Vertex(object):
    """
    Each Vertex uses a dictionary to keep track of the vertices to which it is
     connected, and the weight of each edge.
    """

    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.key) + ' connected To: ' + str(
                [x.key for x in self.connected_to])

    def get_connections(self):
        """
        returns all of the vertices in the adjacency list
        """
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight(self, neighbor):
        """
        :param neighbor: Neighbor Vertex
        :return: weight from current Vertex to neighbor Vertex
        """
        return self.connected_to[neighbor]


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex
        return vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def add_edge(self, _from, _to, cost=0):
        if _from not in self.vertices:
            self.add_vertex(_from)
        if _to not in self.vertices:
            self.add_vertex(_to)
        self.vertices[_from].add_neighbor(self.vertices[_to], cost)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

g = Graph()

for i in range(6):
    g.add_vertex(i)

g.add_edge(0,1,2)
g.add_edge(2,3,5)
for vertex in g:
    print vertex
    print vertex.get_connections()
    print '\n'