import networkx as nx
import matplotlib.pyplot as plt

# NO 1
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


# NO 2
def get_degree(G: nx.Graph, node: int) -> int:
    degrees = G.degree(node)
    return degrees


# NO 3
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    dfs = list(nx.dfs_preorder_nodes(G, source=start))
    return dfs


# NO 4
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    bfs = list(nx.bfs_tree(G, source=start))
    return bfs


# NO 5
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    shortest = nx.shortest_path(G, source=source, target=target)
    return shortest


# NO 6
def visualize_graph(G: nx.Graph) -> None:
    nx.draw(G)
    plt.savefig('graf.png')
