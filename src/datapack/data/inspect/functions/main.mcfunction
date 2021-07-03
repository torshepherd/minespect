# INFO: this function runs every tick

# update functions
execute as @a run function inspect:update_changed_slot
execute as @a run function inspect:update_empty
execute as @a run function inspect:update_idle

# update animations for inspecting players
scoreboard players add @a[tag=inspecting_right] anim_right 1
scoreboard players add @a[tag=inspecting_left] anim_left 1
#execute as @a[tag=start_inspecting_right] run function inspect:right/try_start_animation
#execute as @a[tag=start_inspecting_left] run function inspect:left/try_start_animation
execute as @a[tag=inspecting_right] run function inspect:right/try_update_animation
execute as @a[tag=inspecting_left] run function inspect:left/try_update_animation
tag @a[tag=changed_slot] add reset_right

# reset animations for non-idle players
execute as @a[tag=reset_right] run function inspect:right/try_reset_animation
execute as @a[tag=reset_left] run function inspect:left/try_reset_animation
tag @a[tag=reset_right] remove reset_right
tag @a[tag=reset_left] remove reset_left
