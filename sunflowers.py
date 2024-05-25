from move_util import conv_xy, goto, world_range
from ensure_items import ensure_item
from set_ground import clear_unwanted, ensure

def sunflowers():
    petal_coords = dict()

    for i in world_range():
        x, y = conv_xy(i)
        if x > 0 and y == 0:
            move(East)

        ensure(Entities.Sunflower, Grounds.Soil)
        plant(Entities.Sunflower)

        petals = measure()

        if petals not in petal_coords:
            petal_coords[petals] = list()

        petal_coords[petals].append(i)

        move(North)
    move(East)

    for p in range(15, 0, -1):
        if p in petal_coords:
            while len(petal_coords[p]) > 0:
                i = petal_coords[p].pop(0)
                goto(i)
                if can_harvest():
                    harvest()
                else:
                    petal_coords[p].append(i)


goto(0)
ensure_item(Items.Sunflower_Seed)
sunflowers()
