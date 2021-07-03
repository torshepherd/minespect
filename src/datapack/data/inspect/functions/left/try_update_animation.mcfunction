# INFO: this function tries to set the CustomModelData to an item if already inspecting.

# say Trying to update animation (left)...
execute as @s[nbt={Inventory:[{Slot: -106b, tag:{inspecting:1b}}]}] run function inspect:left/update_animation
