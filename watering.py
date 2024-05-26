# water the ground, buy 1000 more tanks if we ran out
def water():
    while get_water() < 0.95:
        if not use_item(Items.Water_Tank):
            trade(Items.Empty_Tank, 1000)
            break
