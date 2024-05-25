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
    # counterclockwise order
    # left  is idx+1 % 4
    # right is idx-1 % 4
    DIRECTIONS = [North, West, South, East]

    # follow the left wall
    facing_idx = 0

    while get_entity_type() != Entities.Treasure:
        left_idx =  (facing_idx + 1) % 4
        right_idx = (facing_idx - 1) % 4

        # try moving left
        if move(DIRECTIONS[left_idx]):
            facing_idx = left_idx
            
        # can't move left, so try straight
        elif move(DIRECTIONS[facing_idx]):
            # facing_idx = facing_idx
            pass

        # can't move straight, try right
        elif move(DIRECTIONS[right_idx]):
            facing_idx = right_idx

        # turn around
        else:
            back_idx = (facing_idx + 2) % 4
            if not move(DIRECTIONS[back_idx]):
                print("HELP I AM STUCK")
            facing_idx = back_idx

    #do_a_flip()
    harvest()

while True:
    plant_maze()
    # random_solve()
    left_wall_solve()
