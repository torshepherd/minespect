# INFO: this function stores a tick counter scoreboard value to the CustomModelData of an inspecting item

execute store result storage inspect:slide value int 1 run scoreboard players get @s anim_right
item entity @s weapon.mainhand modify inspect:increment_model_data

#tellraw @s ["",{"text":"UPDATE_ANIM: "},{"score":{"name":"exotic_sangria","objective":"check_right"}},{"score":{"name":"exotic_sangria","objective":"anim_right"}},{"nbt":"value","storage":"inspect:slide"}]

#say Updated animation
