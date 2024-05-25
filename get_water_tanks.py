TARGET = 1000

while num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) < TARGET:
    trade(Items.Empty_Tank)