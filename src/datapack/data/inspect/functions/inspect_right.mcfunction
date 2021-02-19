# say Inspecting

execute as @s[tag=inspecting_right] run function inspect:reset_models

tag @s add inspecting_right

scoreboard players set @s inspect_anim 0
function inspect:start_animation_right
