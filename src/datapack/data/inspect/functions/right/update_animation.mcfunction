# INFO: this function stores a tick counter scoreboard value to the CustomModelData of an inspecting item

execute store result storage inspect:slide value int 1 run scoreboard players get @s anim_right
execute if score @s anim_right matches ..0 run data modify storage inspect:slide value set value 0
item entity @s weapon.mainhand modify inspect:increment_model_data
