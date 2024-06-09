def print_all_unlocks():

    quick_print_unlock(Unlocks.Expand)
    quick_print_unlock(Unlocks.Speed)
    quick_print_unlock(Unlocks.Grass)

    quick_print("------")

    quick_print_unlock(Unlocks.Plant)
    quick_print_unlock(Unlocks.Carrots)
    quick_print_unlock(Unlocks.Pumpkins)
    quick_print_unlock(Unlocks.Fertilizer)
    quick_print_unlock(Unlocks.Trees)

    quick_print_unlock(Unlocks.Mazes)
    quick_print_unlock(Unlocks.Cactus)

    quick_print_unlock(Unlocks.Sunflowers)
    quick_print_unlock(Unlocks.Polyculture)

    quick_print_unlock(Unlocks.Dinosaurs)

    # Final unlock
    quick_print_unlock(Unlocks.Leaderboard)

def quick_print_unlock(unlock):
    quick_print(unlock, num_unlocked(unlock), get_cost(unlock))



# All unlocked in leaderboard mode
# quick_print("----- Should be unlocked already")
# quick_print(Unlocks.Auto_Unlock, num_unlocked(Unlocks.Auto_Unlock))
# quick_print(Unlocks.Benchmark, num_unlocked(Unlocks.Benchmark))
# quick_print(Unlocks.Costs, num_unlocked(Unlocks.Costs))
# quick_print(Unlocks.Debug, num_unlocked(Unlocks.Debug))
# quick_print(Unlocks.Debug_2, num_unlocked(Unlocks.Debug_2))
# quick_print(Unlocks.Dictionaries, num_unlocked(Unlocks.Dictionaries))
# quick_print(Unlocks.Functions, num_unlocked(Unlocks.Functions))
# quick_print(Unlocks.Lists, num_unlocked(Unlocks.Lists))
# quick_print(Unlocks.Loops, num_unlocked(Unlocks.Loops))
# quick_print(Unlocks.Multi_Trade, num_unlocked(Unlocks.Multi_Trade))
# quick_print(Unlocks.Operators, num_unlocked(Unlocks.Operators))
# quick_print(Unlocks.Senses, num_unlocked(Unlocks.Senses))
# quick_print(Unlocks.Utilities, num_unlocked(Unlocks.Utilities))
# quick_print(Unlocks.Variables, num_unlocked(Unlocks.Variables))
# quick_print(Unlocks.Watering, num_unlocked(Unlocks.Watering))
