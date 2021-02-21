execute store result score @s check_left run data get entity @s Inventory[-1].tag.CustomModelData
execute if score @s check_left < @s anim_left run tag @s remove idle_left
execute if score @s check_left > @s anim_left run tag @s remove idle_left

tag @s[nbt=!{Inventory:[{Slot: -106b, tag:{inspecting:2b}}]}] remove idle_left
