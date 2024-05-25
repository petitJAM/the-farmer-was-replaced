# Ensures there are at least world_size^2 items, aka one per tile
#
# returns True if either there was already enough, or some amount was purchased successfully
# returns False if there was not enough and none could be purchased
def ensure_item(item):
    if num_items(item) < get_world_size()**2:
        return trade(item, get_world_size()**2)
    return True
