tag @s[tag=changed_slot] remove changed_slot

execute store result score @s current_slot run data get entity @s SelectedItemSlot
execute if score @s current_slot < @s prev_slot run tag @s add changed_slot
execute if score @s current_slot > @s prev_slot run tag @s add changed_slot
