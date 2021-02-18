# say Inspecting

execute as @s[tag=inspecting] run function inspect:reset_models

tag @s add inspecting

scoreboard players set @s inspect_anim 0
function inspect:start_animation
