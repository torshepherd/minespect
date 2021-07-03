# INFO: this function stores a tick counter scoreboard value to the CustomModelData of an inspecting item

execute store result storage inspect:slide value int 1 run scoreboard players get @s anim_right
item entity @s weapon.mainhand modify inspect:increment_model_data
execute at @s anchored eyes run particle minecraft:smoke ^-0.45 ^-.2 ^.5 .01 0.01 .01 .01 1 force
#tellraw @s ["",{"text":"UPDATE_ANIM: "},{"score":{"name":"exotic_sangria","objective":"check_right"}},{"score":{"name":"exotic_sangria","objective":"anim_right"}},{"nbt":"value","storage":"inspect:slide"}]

#say Updated animation
