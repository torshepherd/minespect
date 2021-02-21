# say Inspecting

#execute as @s[tag=inspecting_right] run function inspect:reset_models

function inspect:right/tag_add_inspecting

scoreboard players set @s inspect_anim 0

# Only run this if the item isn't already started
function inspect:right/try_start_animation
