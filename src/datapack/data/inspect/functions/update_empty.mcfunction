tag @s remove emptied_right
tag @s remove emptied_left
tag @s remove filled_right
tag @s remove filled_left

# If nothing selected but previously were not empty, have emptied their hand
tag @s[tag=!empty_right, nbt=!{SelectedItem:{}}] add emptied_right
tag @s[tag=!empty_left, nbt=!{Inventory:[{Slot: -106b}]}] add emptied_left

# If something selected but previously not empty, have filled their hand
tag @s[tag=empty_right, nbt={SelectedItem:{}}] add filled_right
tag @s[tag=empty_left, nbt={Inventory:[{Slot: -106b}]}] add filled_left

# Update empty tags
tag @s remove empty_right
tag @s remove empty_left
tag @s[nbt=!{SelectedItem:{}}] add empty_right
tag @s[nbt=!{Inventory:[{Slot: -106b}]}] add empty_left

# execute as @s[tag=emptied_right] run say emptied_right
# execute as @s[tag=emptied_left] run say emptied_left
# execute as @s[tag=filled_right] run say filled_right
# execute as @s[tag=filled_left] run say filled_left

tag @s[tag=filled_right] add reset_right
tag @s[tag=filled_left] add reset_left

# TODO: add emptied tags for when the count decreases, filled when the count increases.
