from collections import defaultdict

connections = [
    "kh-tc", "qp-kh", "de-cg", "ka-co", "yn-aq", "qp-ub",
    "cg-tb", "vc-aq", "tb-ka", "wh-tc", "yn-cg", "kh-ub",
    "ta-co", "de-co", "tc-td", "tb-wq", "wh-td", "ta-ka",
    "td-qp", "aq-cg", "wq-ub", "ub-vc", "de-ta", "wq-aq",
    "wq-vc", "wh-yn", "ka-de", "kh-ta", "co-tc", "wh-qp",
    "tb-vc", "td-yn"
]

def build_graph(connections):
    graph = defaultdict(set)
    for connection in connections:
        a, b = connection.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                    triangle = tuple(sorted([node, neighbor1, neighbor2]))
                    triangles.add(triangle)
    return triangles

def filter_triangles_with_t(triangles):
    filtered = [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]
    return filtered

network_graph = build_graph(connections)

triangles = find_triangles(network_graph)

triangles_with_t = filter_triangles_with_t(triangles)

print("Triângulos contendo pelo menos um computador que começa com 't':")
for triangle in sorted(triangles_with_t):
    print(','.join(triangle))

print(f"\nQuantidade de triângulos encontrados: {len(triangles_with_t)}")

