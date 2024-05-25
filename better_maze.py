from build_maze import plant_maze
from move_util import conv_idx

directions = {North,South,East,West}
rot_left = {North:West, West:South, South:East, East:North}
rot_right = {North:East, East:South, South:West, West:North}
rot_back = {North:South, South:North, West:East, East:West}

def walk_maze():
    # list? or dictionary?
    # list of tuples maybe
    visited = dict()
    world_size = get_world_size()**2

    treasure_pos = None
    next_treasure_pos = None

    facing = North
    while len(visited) < world_size:
        pos = conv_idx(get_pos_x(), get_pos_y())

        measurement = measure()
        if measurement != None:
            treasure_pos = pos
            next_treasure_pos = conv_idx(measurement[0], measurement[1]) # type: ignore[reportIndexIssue]
            quick_print(measurement)
            quick_print(next_treasure_pos)

        neighbors = check_neighbors()

        visited[pos] = {
            "neighbors": neighbors,
        }

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

    quick_print("I visited:", visited)

    return visited, treasure_pos, next_treasure_pos


def check_neighbors():
    neighbors = dict()
    for d in directions:
        if move(d):
            idx = conv_idx(get_pos_x(), get_pos_y())
            neighbors[d] = idx
            move(rot_back[d])
    return neighbors


if get_entity_type() != Entities.Hedge:
    plant_maze()
v, t, n = walk_maze()
