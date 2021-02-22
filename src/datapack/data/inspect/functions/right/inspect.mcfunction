# INFO: this function should only be called by inspect:inspect

# say Inspecting (right only)
function inspect:right/tag_add_inspecting
scoreboard players set @s anim_right 0
function inspect:right/try_start_animation
function inspect:right/update_animation
