execute store result score @s check_right run data get entity @s SelectedItem.tag.CustomModelData
execute if score @s check_right < @s anim_right run tag @s remove idle_right
execute if score @s check_right > @s anim_right run tag @s remove idle_right
execute if score @s check_right < @s anim_right run tag @s remove idle_left
execute if score @s check_right > @s anim_right run tag @s remove idle_left
# TODO: Make this better. Currently allow CustomModelData of 1 to add back idle ( unless score @s check_right matches 1)

tag @s[nbt=!{SelectedItem:{tag:{inspecting:1b}}}] remove idle_right
tag @s[nbt=!{SelectedItem:{tag:{inspecting:1b}}}] remove idle_left

#tellraw @s ["",{"text":"UPDATE_IDLE: "},{"score":{"name":"exotic_sangria","objective":"check_right"}},{"score":{"name":"exotic_sangria","objective":"anim_right"}}]
