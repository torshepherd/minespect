# Mark as idle, then remove later if needed
execute as @s[tag=!idle_right] run tag @s add idle_right
execute as @s[tag=!idle_left] run tag @s add idle_left

# Check if changed slot, then remove idle_right
execute store result score @s current_slot run data get entity @s SelectedItemSlot
execute if score @s current_slot < @s prev_slot run tag @s remove idle_right
execute if score @s current_slot > @s prev_slot run tag @s remove idle_right

# Check if swapped hands, then remove idle_right and idle_left
#

# Check if holding empty item, then remove idle_right
execute unless data entity @s SelectedItem run tag @s remove idle_right
execute unless data entity @s SelectedItem run say Not holding anything

# Check if holding empty item in offhand, then remove idle_left
#

# DEBUG: broadcast if not idle
execute as @s[tag=!idle_right] run say Not idle!
