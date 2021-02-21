# INFO: this function should only be called by inspect:inspect

say Inspecting (left only)
function inspect:left/tag_add_inspecting
scoreboard players set @s anim_left 0
function inspect:left/try_start_animation
