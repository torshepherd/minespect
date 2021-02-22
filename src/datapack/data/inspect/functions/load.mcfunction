# INFO: this function runs every time the datapack is reloaded

# reset player tags
execute as @a run function inspect:right/tag_remove_inspecting
execute as @a run function inspect:left/tag_remove_inspecting

tag @a remove idle_right
tag @a remove idle_left

tag @a remove changed_slot
tag @a remove swapped_hands

# add scoreboard to track inspect animation frame number
scoreboard objectives add anim_left dummy
scoreboard objectives add anim_right dummy
scoreboard objectives add check_left dummy
scoreboard objectives add check_right dummy

# add scoreboards to track current and previous SelectedItemSlot by players
scoreboard objectives add prev_slot dummy
scoreboard objectives add current_slot dummy

# init prev_slot to zero
execute as @a store result score @s current_slot run data get entity @s SelectedItemSlot
execute as @a run scoreboard players operation @s prev_slot = @s current_slot

tellraw @p {"text":"Click to inspect your current item.","underlined": true,"color":"aqua","clickEvent":{"action":"run_command","value":"/function inspect:inspect"},"hoverEvent":{"action":"show_text","contents":{"text":"function inspect:inspect","bold":true,"color":"aqua"}}}
