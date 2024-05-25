from move_util import conv_xy

# def do_at_each(x, y)
def walk_and_do_with_xy(do_at_each):
    for i in range(get_world_size() ** 2):
        x, y = conv_xy(i)
        if y == 0 and x > 0:
            move(East)
        posx = get_pos_x()
        posy = get_pos_y()

        do_at_each(posx, posy)

        move(North)
    move(East)

def walk_and_do(do_at_each):
    def do_with_xy(x, y):
        do_at_each()

    walk_and_do_with_xy(do_with_xy)
