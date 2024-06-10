from maze_util import plant_maze, travel_path_and_update, walk_maze
from move_util import conv_idx, get_pos_idx
from treat_land import fertilize_old


def bfs(graph, start, end):
    queue = list()
    queue.append([(None, start)])

    visited = set()

    pre_op_count = get_op_count()

    while len(queue) > 0:
        # (dir, idx)
        path = queue.pop(0)
        node = path[-1]
        idx = node[1]

        if idx == end:
            quick_print("BFS total op count:", get_op_count() - pre_op_count)
            return path

        elif node not in visited:
            for neighbor in graph[idx]["neighbors"]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

            visited.add(node)

    quick_print("NO PATH FOUND")
    return []


def gold():
    if get_entity_type() not in [Entities.Hedge, Entities.Treasure]:
        plant_maze()

    graph, treasure_pos = walk_maze()

    quick_print(graph)

    for i in range(300):
        quick_print("Search iteration", i)

        pos = get_pos_idx()
        path = bfs(graph, pos, treasure_pos)
        travel_path_and_update(path, graph)
        measurement = measure()

        if measurement != None:
            x, y = measurement # pyright: ignore
            treasure_pos = conv_idx(x, y)

            while get_entity_type() == Entities.Treasure:
                fertilize_old()

    if get_entity_type() == Entities.Treasure:
        harvest()
    else:
        quick_print("we goofed")
        quick_print("treasure_pos", treasure_pos)

gold()
