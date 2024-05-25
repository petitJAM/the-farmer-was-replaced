def water():
    while get_water() < 1 and num_items(Items.Water_Tank) > 0:
        use_item(Items.Water_Tank)

def fertilize():
    if num_items(Items.Fertilizer) < get_world_size()**2:
        trade(Items.Fertilizer, get_world_size()**2)
    use_item(Items.Fertilizer)
