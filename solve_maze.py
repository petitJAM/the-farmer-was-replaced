from build_maze import plant_maze

def random_solve():
    DIRECTIONS = [North, West, South, East]
    while get_entity_type() != Entities.Treasure:
        dir_idx = random() * 4 // 1
        dir = DIRECTIONS[dir_idx]
        quick_print(dir)
        move(dir)

    do_a_flip()
    harvest()

def left_wall_solve():
    rot_left = {North:West, West:South, South:East, East:North}
    rot_right = {North:East, East:South, South:West, West:North}
    rot_back = {North:South, South:North, West:East, East:West}

    facing = North

    while get_entity_type() != Entities.Treasure:
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

    #do_a_flip()
    harvest()

while True:
    plant_maze()
    # random_solve()
    left_wall_solve()
