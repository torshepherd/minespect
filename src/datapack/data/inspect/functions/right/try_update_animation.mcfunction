# INFO: this function tries to set the CustomModelData to an item if already inspecting.

# say Trying to update animation (right)...
execute as @s[nbt={SelectedItem:{tag:{inspecting:1b}}}] run function inspect:right/update_animation
