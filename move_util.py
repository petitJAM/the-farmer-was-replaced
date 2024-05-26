def world_range():
    return range(get_world_size()**2)

def goto(idx):
    if idx > get_world_size()**2:
        quick_print("idx out of bounds", idx)
        return range(get_world_size()**2)[idx]

    destx, desty = conv_xy(idx)
    half_size = get_world_size() // 2
    startx = get_pos_x()
    starty = get_pos_y()

    startx_is_wester = startx < destx
    betweenx_is_shorter = abs(destx - startx) < half_size

    if startx_is_wester == betweenx_is_shorter:
        dirx = East
    else:
        dirx = West

    while get_pos_x() != destx:
        move(dirx)

    starty_is_souther = starty < desty
    betweeny_is_shorter = abs(desty - starty) < half_size

    if starty_is_souther == betweeny_is_shorter:
        diry = North
    else:
        diry = South

    while get_pos_y() != desty:
        move(diry)

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
