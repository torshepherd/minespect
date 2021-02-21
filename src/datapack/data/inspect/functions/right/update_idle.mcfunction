execute store result score @s check_right run data get entity @s SelectedItem.tag.CustomModelData
execute if score @s check_right < @s anim_right run tag @s remove idle_right
execute if score @s check_right > @s anim_right run tag @s remove idle_right

tag @s[nbt=!{SelectedItem:{tag:{inspecting:1b}}}] remove idle_right
