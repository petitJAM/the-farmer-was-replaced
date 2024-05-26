from build_maze import plant_maze
from move_util import conv_idx, get_pos_idx, travel_path
from treat_land import fertilize_old

directions = {North,South,East,West}
rot_left = {North:West, West:South, South:East, East:North}
rot_right = {North:East, East:South, South:West, West:North}
rot_back = {North:South, South:North, West:East, East:West}

# The initial walk of the maze to build a graph
def walk_maze():
    rot_left = {North:West, West:South, South:East, East:North}
    rot_right = {North:East, East:South, South:West, West:North}
    rot_back = {North:South, South:North, West:East, East:West}

    visited = dict()
    world_size = get_world_size()**2

    treasure_pos = None

    facing = North
    while len(visited) < world_size:
        pos = conv_idx(get_pos_x(), get_pos_y())

        measurement = measure()
        if measurement != None:
            treasure_pos = pos

        if pos not in visited:
            visited[pos] = {"neighbors": check_neighbors()}

        left = rot_left[facing]
        right = rot_right[facing]

        if move(left):
            facing = left

        elif move(facing):
            facing = facing

        elif move(right):
            facing = right

        else:
            back = rot_back[facing]
            if not move(back):
                print("HELP I AM STUCK")
            facing = back

    return visited, treasure_pos

def check_neighbors():
    directions = {North,South,East,West}
    rot_back = {North:South, South:North, West:East, East:West}

    neighbors = list()
    for d in directions:
        if move(d):
            neighbors.append(get_pos_idx())
            move(rot_back[d])
    return neighbors

def bfs(graph, start, end):
    queue = list()
    queue.append([start])

    visited = set()

    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            return path

        elif node not in visited:
            for neighbor in graph[node]["neighbors"]:
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

    for i in range(299):
        quick_print("Treasure iteration", i+1)
        pos = get_pos_idx()
        path = bfs(graph, pos, treasure_pos)
        travel_path(path)
        x, y = measure() # type: ignore
        next_treasure_pos = conv_idx(x, y)

        while get_entity_type() == Entities.Treasure:
            fertilize_old()

        treasure_pos = next_treasure_pos

    harvest()

gold()
