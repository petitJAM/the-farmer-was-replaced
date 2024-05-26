# Returns True if fertilize was successful or trade then fertilize was successful
# Returns False if the trade for more failed
def fertilize():
    used = use_item(Items.Fertilizer) 

    if not used:
        trade(Items.Fertilizer, get_world_size()**2)
        used = use_item(Items.Fertilizer) 

    return used
