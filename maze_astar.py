from better_maze import walk_maze
from build_maze import plant_maze
from fertilizing import fertilize
from move_util import conv_idx, conv_xy, get_pos_idx, goto


def astar(graph, start, goal, heuristic):
    open_set = {start}

    came_from = dict()

    g_score = dict() # default val infinity
    g_score[start] = 0

    f_score = dict() # default val infinity
    f_score[start] = heuristic(start, goal)

    while len(open_set) > 0:
        open_set_as_list = list(open_set)
        current = open_set_as_list[0]
        # Find the max by f_score
        for node in open_set_as_list:
            if f_score[node] > f_score[current]:
                current = node

        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)

        for neighbor in graph[current]["neighbors"]:
            # TODO: weight of edge? probably doesn't matter? everything is 1?
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                if neighbor not in open_set:
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


def maze():
    graph, treasure_pos = walk_maze()

    #set_execution_speed(5)

    for i in range(299):
        start = get_pos_idx()
        path = astar(graph, start, treasure_pos, heuristic)
        for p in path:
            goto(p)

        x, y = measure() # pyright: ignore
        treasure_pos = conv_idx(x, y)

        while get_entity_type() == Entities.Treasure:
            fertilize()

    harvest()


# set_farm_size(4)
plant_maze()
maze()
