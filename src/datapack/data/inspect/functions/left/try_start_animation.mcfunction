# INFO: this function tries to set the attack speed, hide modifiers, and set item tag of inspecting:1b to an item if not already inspecting.

say Trying to start animation (left)...
execute as @s[nbt=!{Inventory:[{Slot: -106b, tag:{inspecting:1b}}]}] run function inspect:left/start_animation
