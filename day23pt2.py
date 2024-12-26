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

def bron_kerbosch(graph, R, P, X, cliques):
    if not P and not X: 
        cliques.append(R)
        return
    for v in list(P): 
        bron_kerbosch(
            graph,
            R.union({v}),  
            P.intersection(graph[v]), 
            X.intersection(graph[v]),   
            cliques
        )
        P.remove(v)  
        X.add(v)    

def find_largest_clique_bk(graph):
    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(graph, set(), nodes, set(), cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique

network_graph = build_graph(connections)

largest_clique = find_largest_clique_bk(network_graph)

password = ','.join(sorted(largest_clique))

print(f"A senha para entrar na LAN party é: {password}")
