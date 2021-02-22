# INFO: this function stores a tick counter scoreboard value to the CustomModelData of an inspecting item

scoreboard players add @s anim_right 1

execute store result storage inspect:slide value int 1 run scoreboard players get @s anim_right
#execute if score @s anim_right matches ..0 run data modify storage inspect:slide value set value 0

#tellraw @s ["",{"text":"UPDATE_ANIM: "},{"score":{"name":"exotic_sangria","objective":"check_right"}},{"score":{"name":"exotic_sangria","objective":"anim_right"}},{"nbt":"value","storage":"inspect:slide"}]
item entity @s weapon.mainhand modify inspect:increment_model_data

#say Updated animation
