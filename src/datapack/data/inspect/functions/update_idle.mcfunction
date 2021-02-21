# Mark as idle, then remove later if needed
execute as @s[tag=!idle_right] run tag @s add idle_right
execute as @s[tag=!idle_left] run tag @s add idle_left
tag @s remove idle_left
# fix later ^

# Check if inventory changed (in an unexpected way), then remove idle_right and idle_left

# Check if changed slot, then remove idle_right
tag @s[tag=changed_slot] remove idle_right

# Check if swapped hands, then remove idle_right and idle_left
#

# Check if holding empty item, then remove idle_right
execute unless data entity @s SelectedItem run tag @s remove idle_right
# execute unless data entity @s SelectedItem run say Not holding anything

# Check if holding empty item in offhand, then remove idle_left
#

# reset models for non-idle inspecting players
execute as @s[tag=inspecting_right, tag=!idle_right] run function inspect:right/tag_remove_inspecting
execute as @s[tag=inspecting_left, tag=!idle_left] run tag @s remove inspecting_left
execute as @s[tag=inspecting_both, tag=!idle_right] run tag @s remove inspecting_both
execute as @s[tag=inspecting_both, tag=!idle_left] run tag @s remove inspecting_both

# DEBUG: broadcast if not idle
# execute as @s[tag=!idle_right] run say Not idle!
