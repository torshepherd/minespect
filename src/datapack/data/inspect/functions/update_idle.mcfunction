# Mark as idle, then remove later if needed
execute as @s[tag=!idle_right] run tag @s add idle_right
execute as @s[tag=!idle_left] run tag @s add idle_left

# Check if inventory changed (in an unexpected way), then remove idle_right and idle_left

# Check if changed slot, then remove idle_right and idle_left
tag @s[tag=changed_slot] remove idle_right
tag @s[tag=changed_slot] remove idle_left

# Check if swapped hands, then remove idle_right and idle_left
tag @s[tag=swapped_hands] remove idle_right
tag @s[tag=swapped_hands] remove idle_left

# Check if holding empty item in either hand, then remove idle for that hand
tag @s[tag=empty_right] remove idle_right
tag @s[tag=empty_left] remove idle_left

# If dropped or picked up either hand, stop animating both
tag @s[tag=emptied_right] remove idle_left
tag @s[tag=filled_right] remove idle_left
tag @s[tag=emptied_left] remove idle_right
tag @s[tag=filled_left] remove idle_right

# reset models for non-idle inspecting players
tag @s[tag=inspecting_right, tag=!idle_right] add reset_right
tag @s[tag=inspecting_left, tag=!idle_left] add reset_left
execute as @s[tag=inspecting_right, tag=!idle_right] run function inspect:right/tag_remove_inspecting
execute as @s[tag=inspecting_left, tag=!idle_left] run function inspect:left/tag_remove_inspecting

# DEBUG: broadcast if not idle
# execute as @s[tag=!idle_right] run say Not idle!
