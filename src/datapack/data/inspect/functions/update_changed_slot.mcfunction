# INFO: this function runs every tick, and tags players who have changed slots

# store current item slots in prev_slot
scoreboard players operation @s prev_slot = @s current_slot
tag @s[tag=changed_slot] remove changed_slot

execute store result score @s current_slot run data get entity @s SelectedItemSlot
execute if score @s current_slot < @s prev_slot run tag @s add changed_slot
execute if score @s current_slot > @s prev_slot run tag @s add changed_slot

# execute as @s[tag=changed_slot] run say Changed slot!
