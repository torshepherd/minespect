execute as @a run function inspect:right/tag_remove_inspecting
tag @a remove inspecting_left
tag @a remove inspecting_both

tag @a add not_inspecting_left
tag @a add not_inspecting_both

tag @a remove idle_right
tag @a remove idle_left

scoreboard objectives add inspect_anim minecraft.custom:minecraft.time_since_death
scoreboard objectives add prev_slot dummy
scoreboard objectives add current_slot dummy

scoreboard players set @a prev_slot 0

tellraw @p {"text":"Click to inspect your current item.","underlined": true,"clickEvent":{"action":"run_command","value":"/function inspect:inspect"},"hoverEvent":{"action":"show_text","contents":{"text":"function inspect:inspect","bold":true,"color":"aqua"}}}
