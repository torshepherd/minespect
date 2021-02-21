# update whether a player has just switched active slot
execute as @a run function inspect:update_changed_slot

# check if players are idle
execute as @a run function inspect:update_idle

# update animations for inspecting players
execute as @a[tag=inspecting_right] run function inspect:right/update_animation

# reset animations for non-idle players
execute as @a[tag=changed_slot] run function inspect:right/try_reset_animation

# store current item slots in prev_slot
execute as @a run scoreboard players operation @s prev_slot = @s current_slot
