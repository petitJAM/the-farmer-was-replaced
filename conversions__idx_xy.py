def conv_xy(idx):
    y = idx  % get_world_size()
    x = idx // get_world_size()
    return x, y

def conv_idx(x, y):
    return x * get_world_size() + y

# visual test
for i in range(get_world_size() ** 2):
    x, y = conv_xy(i)
    quick_print(conv_idx(x, y))
