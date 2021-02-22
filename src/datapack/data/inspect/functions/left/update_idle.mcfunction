execute store result score @s check_left run data get entity @s Inventory[-1].tag.CustomModelData
execute if score @s check_left < @s anim_left run tag @s remove idle_left
execute if score @s check_left > @s anim_left run tag @s remove idle_left
execute if score @s check_left < @s anim_left run tag @s remove idle_right
execute if score @s check_left > @s anim_left run tag @s remove idle_right
# TODO: Make this better. Currently allow CustomModelData of 1 to add back idle (unless score @s check_left matches 1)

tag @s[nbt=!{Inventory:[{Slot: -106b, tag:{inspecting:2b}}]}] remove idle_left
tag @s[nbt=!{Inventory:[{Slot: -106b, tag:{inspecting:2b}}]}] remove idle_right

#tellraw @s ["",{"text":"UPDATE_IDLE: "},{"score":{"name":"exotic_sangria","objective":"check_left"}},{"score":{"name":"exotic_sangria","objective":"anim_left"}}]
