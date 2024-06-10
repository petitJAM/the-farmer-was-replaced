def world_range():
    return range(get_world_size()**2)

def goto(idx):
    if idx > get_world_size()**2:
        quick_print("idx out of bounds", idx)
        return range(get_world_size()**2)[idx]
    x, y = conv_xy(idx)
    goto_xy(x, y)

def goto_xy(destx, desty):
    # pre_op_count = get_op_count()
    startx = get_pos_x()
    starty = get_pos_y()
    half_size = get_world_size() // 2

    startx_is_wester = startx < destx
    deltax = abs(destx - startx)
    betweenx_is_shorter = deltax < half_size

    if startx_is_wester == betweenx_is_shorter:
        dirx = East
    else:
        dirx = West

    while get_pos_x() != destx:
        move(dirx)

    starty_is_souther = starty < desty
    deltay = abs(desty - starty)
    betweeny_is_shorter = deltay < half_size

    if starty_is_souther == betweeny_is_shorter:
        diry = North
    else:
        diry = South

    # calc_op_count = get_op_count() - pre_op_count
    # quick_print("goto calc op count:", calc_op_count)

    while get_pos_y() != desty:
        move(diry)

    # move_op_count = get_op_count() - calc_op_count - pre_op_count
    # quick_print("goto move op count:", move_op_count)


def conv_xy(idx):
    y = idx  % get_world_size()
    x = idx // get_world_size()
    return x, y

def conv_idx(x, y):
    return x * get_world_size() + y

def get_pos_idx():
    return conv_idx(get_pos_x(), get_pos_y())

# Traverse a list of indexes
def travel_path(path):
    for idx in path:
        goto(idx)

def manhattan_dist_idx(idx1, idx2):
    xy1 = conv_xy(idx1)
    xy2 = conv_xy(idx2)
    return manhattan_dist_xy(xy1, xy2)

def manhattan_dist_xy(xy1, xy2):
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])
