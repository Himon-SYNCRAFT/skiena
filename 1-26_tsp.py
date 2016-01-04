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
    chains = []
    min_key = min(edges, key=edges.get)
    chains.append(list(min_key))
    del edges[min_key]

    while edges:
        min_key = min(edges, key=edges.get)
        current_edge = list(min_key)
        connected_points = []
        chains_to_remove = []
        for chain_index in range(len(chains)):
            chain = chains[chain_index]
            if current_edge[0] == chain[len(chain) - 1]:
                connected_points.append(current_edge[0])
                chains_to_remove.append(chain_index)
                chain_copy = chain.copy()
                chain_copy.extend(current_edge)
                current_edge = chain_copy
            elif current_edge[0] == chain[0]:
                connected_points.append(current_edge[0])
                chains_to_remove.append(chain_index)
                current_edge.reverse()
                current_edge.extend(chain)
            elif current_edge[1] == chain[len(chain) - 1]:
                connected_points.append(current_edge[1])
                chains_to_remove.append(chain_index)
                chain_copy = chain.copy()
                current_edge.reverse()
                chain_copy.extend(current_edge)
                current_edge = chain_copy
            elif current_edge[1] == chain[0]:
                connected_points.append(current_edge[1])
                chains_to_remove.append(chain_index)
                current_edge.extend(chain)

            print(edges)

        if not connected_points:
            del edges[min_key]
        else:
            for p in connected_points:
                for e in list(edges.keys()):
                    if p in e:
                        print(edges)
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
