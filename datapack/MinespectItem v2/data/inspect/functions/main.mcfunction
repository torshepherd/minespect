# check if players are idle
execute as @a run function inspect:update_idle

# update animations for idle players
execute as @a[tag=inspecting, tag=idle] run function inspect:update_animation

# reset models for non-idle inspecting players
execute as @a[tag=inspecting, tag=!idle] run function inspect:reset_models

# store current item slots in prev_slot
execute as @a run scoreboard players operation @s prev_slot = @s current_slot
