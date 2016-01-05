"""
Implement the two TSP heuristics of Section 1.1 (page 5). Which of them gives
better-quality solutions in practice? Can you devise a heuristic that works better
than both of them?
"""

import unittest


def nearest_neighbor(edges, start_point=0):
    visited = {start_point}
    path = [start_point]
    while edges:
        connected_edges_to_last_point = {}
        for points, distance in list(edges.items()):
            if path[len(path) - 1] in points:
                connected_edges_to_last_point[points] = distance
        if connected_edges_to_last_point:
            next_edge = min(connected_edges_to_last_point,
                            key=connected_edges_to_last_point.get)
            for point in next_edge:
                if point not in visited:
                    visited.add(point)
                    path.append(point)
            for edge in connected_edges_to_last_point.keys():
                del edges[edge]
    return path


def closest_pair(edges):
    """
    1) The description states that every vertex always belongs either to a
    "single-vertex chain" (i.e., it's alone) or it belongs to one other chain;
    a vertex can only belong to one chain. The algorithm says at each step you
    select every possible pair of two vertices which are each an endpoint of the
    respective chain they belong to, and don't already belong to the same chain.
    Sometimes they'll be singletons; sometimes one or both will already belong
    to a non-trivial chain, so you'll join two chains.
    2) You repeat the loop n times, so that you eventually select every vertex;
    but yes, the actual iteration count isn't used for anything.
    All that matters is that you run the loop enough times.
    """
    chains = []

    while edges:
        min_key = min(edges, key=edges.get)
        current_edge = list(min_key)
        connected_points = []
        chains_to_remove = []

        print(chains)
        print("min", current_edge)

        for chain_index in range(len(chains)):
            chain = chains[chain_index]
            if current_edge[0] == chain[len(chain) - 1]:
                connected_points.append(current_edge[0])
                chains_to_remove.append(chain_index)
                chain_copy = chain.copy()
                current_edge.pop(0)
                chain_copy.extend(current_edge)
                current_edge = chain_copy
            elif current_edge[0] == chain[0]:
                connected_points.append(current_edge[0])
                chains_to_remove.append(chain_index)
                current_edge.pop(0)
                current_edge.extend(chain)
            elif current_edge[len(current_edge) - 1] == chain[len(chain) - 1]:
                connected_points.append(current_edge[len(current_edge) - 1])
                chains_to_remove.append(chain_index)
                chain_copy = chain.copy()
                current_edge.pop()
                chain_copy.extend(current_edge)
                current_edge = chain_copy
            elif current_edge[len(current_edge) - 1] == chain[0]:
                connected_points.append(current_edge[len(current_edge) - 1])
                chains_to_remove.append(chain_index)
                current_edge.pop()
                current_edge.extend(chain)
            print("current", current_edge)

        if not connected_points:
            del edges[min_key]
        else:
            for p in connected_points:
                for e in list(edges.keys()):
                    if p in e:
                        del edges[e]

            chains_to_remove.sort()
            chains_to_remove.reverse()
            for i in chains_to_remove:
                del chains[i]

        chains.append(current_edge)

    return chains



def points_to_edges():
    pass


if __name__ == "__main__":

    edges = {
        (0, 1): 2,
        (0, 2): 3,
        (0, 3): 4,
        (1, 2): 4,
        (1, 3): 3,
        (2, 3): 2
    }

    print(closest_pair(edges))
    # unittest.main()
