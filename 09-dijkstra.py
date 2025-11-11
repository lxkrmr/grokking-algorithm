import math


def dijkstra(graph: dict, costs: dict, parents: dict, processed: set):
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs, processed)


def find_lowest_cost_node(costs: dict, processed: set):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        if node in processed:
            continue

        cost = costs[node]
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def extract_path_with_total_costs(parents: dict, costs: dict, start_node= "start", end_node= "fin"):
    total_costs = str(costs[end_node])
    parent = end_node
    path = [end_node]
    while parent is not start_node:
        child = parents[parent]
        path.append(child)
        parent = child

    path.reverse()
    return " -> ".join(path) + " = " + total_costs


def main():
    graph = {
        "start": {
            "a": 6,
            "b": 2,
        },
        "a": {
            "fin": 1,
        },
        "b": {
            "a": 3,
            "fin": 5,
        },
        "fin": {},
    }

    costs = {
        "a": 6,
        "b": 2,
        "fin": math.inf
    }

    parents = {
        "a": "start",
        "b": "start",
        "fin": None,
    }

    processed = set()
    dijkstra(graph, costs, parents, processed)
    print(extract_path_with_total_costs(parents, costs))


if __name__ == '__main__':
    main()
