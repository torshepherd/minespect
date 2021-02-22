# INFO: this function tries to set the attack speed, hide modifiers, and set item tag of inspecting:1b to an item if not already inspecting.

# say Trying to start animation (right)...
execute as @s[nbt=!{SelectedItem:{tag:{inspecting:1b}}}] run function inspect:right/start_animation
