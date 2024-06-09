# pyright: reportOptionalSubscript=false
from debug_unlocks import print_all_unlocks
from move_util import goto, world_range


timed_reset()

print_all_unlocks()
# style on 'em (remove for ez perf gainz)
do_a_flip()

############
# Stage 01 #
############

cost = get_cost(Unlocks.Speed)[Items.Hay] + get_cost(Unlocks.Expand)[Items.Hay]
while num_items(Items.Hay) < cost:
    harvest()
unlock(Unlocks.Speed)
unlock(Unlocks.Expand)

cost = get_cost(Unlocks.Plant)[Items.Hay]
while num_items(Items.Hay) < cost:
    move(North)
    harvest()
unlock(Unlocks.Plant)

cost = get_cost(Unlocks.Expand)[Items.Wood]
while num_items(Items.Wood) < cost:
    if get_entity_type() != Entities.Bush:
        plant(Entities.Bush)
    if can_harvest():
        harvest()
    move(North)
unlock(Unlocks.Expand)

############
# Stage 02 #
############

speed_unlocked = False
carrots_unlocked = False
while not carrots_unlocked:
    for i in world_range():
        goto(i)
        if get_entity_type() != Entities.Bush:
            plant(Entities.Bush)
        if can_harvest():
            harvest()

        if not speed_unlocked and unlock(Unlocks.Speed):
            speed_unlocked = True
        elif speed_unlocked and unlock(Unlocks.Carrots):
            carrots_unlocked = True

############
# Stage 03 #
############

print_all_unlocks()

while True:
    do_a_flip()

unlock(Unlocks.Leaderboard)
timed_reset()
