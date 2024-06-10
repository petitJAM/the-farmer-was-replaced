from fertilizing import fertilize
from maze_util import plant_maze, travel_path_and_update, walk_maze
from move_util import conv_idx, conv_xy, get_pos_idx


def astar(graph, start, goal, heuristic):
    start_node = (None, start)
    open_set = {start_node}

    came_from = dict()

    # {idx: score|inf}
    g_score = dict()
    g_score[start] = 0

    # {idx: score|inf}
    f_score = dict()
    f_score[start] = heuristic(start, goal)

    while len(open_set) > 0:
        quick_print("open_set", len(open_set), open_set)

        open_set_as_list = list(open_set)
        current_node = open_set_as_list[0]
        # Find the max by f_score
        for node in open_set_as_list:
            # node.f < current.f or (node.f == current.f and node.h < current.h)
            if f_score[node[1]] > f_score[current_node[1]]:
                current_node = node

        quick_print("current_node", current_node, f_score[current_node[1]])
        quick_print("came_from", len(came_from), came_from)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        open_set.remove(current_node)

        for neighbor in graph[current_node[1]]["neighbors"]:
            # TODO: weight of edge? probably doesn't matter? everything is 1?
            tentative_g_score = g_score[current_node[1]] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor[1]]:
                came_from[neighbor] = current_node
                g_score[neighbor[1]] = tentative_g_score
                f_score[neighbor[1]] = tentative_g_score + heuristic(neighbor[1], goal)

                if neighbor not in open_set:
                    quick_print("adding neighbor", neighbor)
                    open_set.add(neighbor)

    return "it's all broken"

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def heuristic(node, goal):
    node_x, node_y = conv_xy(node)
    goal_x, goal_y = conv_xy(goal)
    return abs(node_x - goal_x) + abs(node_y - goal_y)


def maze_astar():
    if get_entity_type() not in [Entities.Hedge, Entities.Treasure]:
        plant_maze()

    graph, treasure_pos = walk_maze()

    for i in range(300):
        quick_print("Search iteration", i)

        start = get_pos_idx()
        path = astar(graph, start, treasure_pos, heuristic)
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


# set_farm_size(4)
maze_astar()
