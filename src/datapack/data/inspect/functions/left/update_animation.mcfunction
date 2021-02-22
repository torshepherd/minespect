# INFO: this function stores a tick counter scoreboard value to the CustomModelData of an inspecting item

execute store result storage inspect:slide value int 1 run scoreboard players get @s anim_left
item entity @s weapon.offhand modify inspect:increment_model_data
