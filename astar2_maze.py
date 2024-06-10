from fertilizing import fertilize
from maze_util import plant_maze, travel_path_and_update, walk_maze
from move_util import conv_idx, get_pos_idx, goto, manhattan_dist_idx, world_range


# g cost - dist from node to start node
# h cost - dist from node to goal node

# h = heuristic = manhattan dist

# f = g + h

def astar(graph, start, goal, h):
    start_node = (None, start)
    to_search = [start_node]
    processed = list()

    f_scores = dict()
    g_scores = dict()
    for idx in world_range():
        f_scores[idx] = Infinity
        g_scores[idx] = Infinity

    g_scores = {start: 0}

    came_from = dict()

    while len(to_search) > 0:
        current_node = to_search[0]

        # Choose min f score in to_search
        for node in to_search:
            node_f = f_scores[node[1]]
            curr_f = f_scores[current_node[1]]
            if ((node_f < curr_f) or 
                    (node_f == curr_f and h(node[1], goal) < h(current_node[1], goal))):
                current_node = node

        if current_node[1] == goal:
            quick_print("------------ COMPLETE")
            quick_print(current_node, goal)
            quick_print(len(came_from), came_from)
            for foo in came_from:
                quick_print(foo, came_from[foo])
            return reconstruct_path(came_from, current_node)

        processed.append(current_node[1])
        to_search.remove(current_node)

        quick_print("-------- current_node", current_node)

        for neighbor_node in graph[current_node[1]]['neighbors']:
            if neighbor_node not in processed:
                quick_print("---- processing neighbor", neighbor_node)
                in_search = neighbor_node in to_search

                current_g_score = g_scores[current_node[1]]

                # 1 is dist to neighbor, always fixed value of 1
                neighbor_cost = current_g_score + 1

                quick_print("in_search", in_search, "curr_g_score", current_g_score, "neighbor_cost", neighbor_cost)

                if (not in_search) or (neighbor_cost < g_scores[neighbor_node[1]]):

                    g_scores[neighbor_node[1]] = neighbor_cost

                    if neighbor_node in came_from:
                        quick_print("OVERWRITING", neighbor_node, came_from[neighbor_node], "with", current_node)
                    came_from[neighbor_node] = current_node

                    quick_print("add g_scores[", neighbor_node[1], "] = ", neighbor_cost)
                    quick_print("add came_from[", neighbor_node, "] = ", current_node)

                    # can this move up out of the parent if?
                    if not in_search:
                        f_scores[neighbor_node[1]] = neighbor_cost + h(neighbor_node[1], goal)
                        to_search.append(neighbor_node)
                        quick_print("add f_scores[", neighbor_node[1], "] = ", f_scores[neighbor_node[1]])

            else:
                quick_print("skipping neighbor", neighbor_node)


def reconstruct_path(came_from, current):
    quick_print("Reconstructing", current, came_from)
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
        quick_print(total_path)
    return total_path


def maze_astar2():
    if get_entity_type() not in [Entities.Hedge, Entities.Treasure]:
        plant_maze()

    graph, treasure_pos = walk_maze()

    for i in range(300):
        quick_print("Search iteration", i)

        start = get_pos_idx()
        path = astar(graph, start, treasure_pos, manhattan_dist_idx)
        travel_path_and_update(path, graph)
        measurement = measure()

        if measurement != None:
            x, y = measurement # pyright: ignore
            treasure_pos = conv_idx(x, y)

            while get_entity_type() == Entities.Treasure:
                fertilize()

    if get_entity_type() == Entities.Treasure:
        harvest()
    else:
        quick_print("we goofed")
        quick_print("treasure_pos", treasure_pos)


set_farm_size(4)
goto(0)
maze_astar2()
