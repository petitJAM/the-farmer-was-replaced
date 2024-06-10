from fertilizing import fertilize
from move_util import conv_idx, get_pos_idx


def plant_maze():
    if get_entity_type() == Entities.Hedge:
        return

    if get_ground_type() != Grounds.Turf:
        till()
    plant(Entities.Bush)

    while get_entity_type() != Entities.Hedge:
        fertilize()


# The initial walk of the maze to build a graph
#
# {
#   idx: {'neighbors': [(dir, idx), ...], 'walls': [dir, ...]},
#   ...
# }
def walk_maze():
    dir_dicts = get_dir_dicts()
    rot_left = dir_dicts["rot_left"]
    rot_right = dir_dicts["rot_right"]
    rot_back = dir_dicts["rot_back"]

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
            visited[pos] = get_neighbors()

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


# {
#   'neighbors': [(direction, idx), ...],
#   'walls': [direction, ...],
# }
def get_neighbors():
    dir_dicts = get_dir_dicts()
    directions = dir_dicts["directions"]
    rot_back = dir_dicts["rot_back"]

    neighbors = list()
    walls = list()
    for d in directions:
        if move(d):
            neighbors.append((d, get_pos_idx()))
            move(rot_back[d])
        else:
            walls.append(d)
    return {'neighbors': neighbors, 'walls': walls}


def get_dir_dicts():
    return {
        "directions": {North,South,East,West},
        "rot_left": {North:West, West:South, South:East, East:North},
        "rot_right": {North:East, East:South, South:West, West:North},
        "rot_back": {North:South, South:North, West:East, East:West},
    }


# path - [(dir, idx), ...]
# graph - see walk_maze
def travel_path_and_update(path, graph):
    rot_back = get_dir_dicts()["rot_back"]

    # Pop the initial node off since we're already there (and its direction is None)
    node = path.pop(0)
    update_current_node(graph, node[1], rot_back)

    for tup in path:
        move(tup[0])
        update_current_node(graph, tup[1], rot_back)


def update_current_node(graph, idx, rot_back):
    for d in graph[idx]['walls']:
        if move(d):
            graph[idx]['walls'].remove(d)
            graph[idx]['neighbors'].append((d, get_pos_idx()))
            move(rot_back[d])
