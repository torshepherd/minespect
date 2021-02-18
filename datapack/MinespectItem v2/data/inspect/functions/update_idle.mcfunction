# Mark as idle, then remove later if needed
execute as @s[tag=!idle] run tag @s add idle

# Check if changed slot, then remove idle
execute store result score @s current_slot run data get entity @s SelectedItemSlot
execute if score @s current_slot > @s prev_slot run tag @s remove idle
execute if score @s current_slot < @s prev_slot run tag @s remove idle
# scoreboard players operation @s prev_slot = @s current_slot

# Check if holding empty item, then remove idle
execute unless data entity @s SelectedItem run tag @s remove idle

# DEBUG: broadcast if not idle
# execute as @s[tag=!idle] run say Not idle!
